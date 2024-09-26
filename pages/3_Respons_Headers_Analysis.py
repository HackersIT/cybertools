import streamlit as st
import requests
import pandas as pd

# Function to check for security headers
def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
    except Exception as e:
        st.error(f"Error fetching the URL: {e}")
        return None

    # Define common security headers to check
    security_headers = {
        'Strict-Transport-Security': 'HSTS',
        'Content-Security-Policy': 'CSP',
        'X-Content-Type-Options': 'XCTO',
        'X-Frame-Options': 'XFO',
        'Referrer-Policy': 'RP',
        'Permissions-Policy': 'PP',
        'X-XSS-Protection': 'X-XSS'
    }

    results = []

    # Check headers in the response
    for header, name in security_headers.items():
        value = headers.get(header, None)
        if value:
            results.append([header, value, 'Not Vulnerable'])
        else:
            results.append([header, 'Missing', 'Vulnerable'])

    return results

# Streamlit UI
st.title("Security Header Scanner")

# Input URL
url = st.text_input("Enter the URL (with http:// or https://):")

if url:
    # Fetch header results
    header_results = check_security_headers(url)

    if header_results:
        # Create a DataFrame
        df = pd.DataFrame(header_results, columns=['Header', 'Value', 'Vulnerability Status'])

        # Function to apply styles
        def highlight_vulnerabilities(val):
            color = 'red' if val == 'Vulnerable' else 'blue'
            return f'color: {color}'

        # Display table
        st.write("### Security Headers Check")
        st.dataframe(df.style.applymap(highlight_vulnerabilities, subset=['Vulnerability Status']))

