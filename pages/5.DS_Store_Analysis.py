import streamlit as st
import requests
from urllib.parse import urlparse
from io import BytesIO
from ds_store import DSStore

# Function to download .DS_Store file from the provided URI
def download_ds_store(uri):
    response = requests.get(uri, verify=False)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        st.error("Failed to download the file. Please check the URI.")
        return None

# Function to extract entries from .DS_Store file
def extract_ds_store(file_data):
    extracted_data = []
    try:
        with DSStore.open(file_data) as ds_store:
            for entry in ds_store:
                extracted_data.append({
                    'filename': entry.filename,
                    'code': entry.code,
                    'type': entry.type,
                    'value': entry.value
                })
        return extracted_data
    except Exception as e:
        st.error(f"Error reading .DS_Store file: {e}")
        return None

# Function to extract hostname from URI
def extract_hostname(uri):
    parsed_uri = urlparse(uri)
    return f"{parsed_uri.scheme}://{parsed_uri.netloc}"

# Streamlit App
st.title("DS_Store File Analysis")

# Input field for the .DS_Store URI
st.markdown('''
The `.DS_Store` file is created by macOS to store custom attributes of a folder, such as icon positions, view settings, etc. Sometimes, it can unintentionally leak information about the folder’s contents, including hidden or sensitive files and directories.''')
uri = st.text_input("Enter the URI of the .DS_Store file:",placeholder="https://www.vulnweb.com/.DS_Store")

if uri:
    # Extract the hostname from the URI
    hostname = extract_hostname(uri)
    
    file_data = download_ds_store(uri)
    
    if file_data:
        extracted_data = extract_ds_store(file_data)
        
        if extracted_data:
            st.success("DS_Store file data extracted successfully!")
            
            # Generate URLs by appending filenames to the hostname
            st.write("Generated URLs:")
            for entry in extracted_data:
                filename_url = f"{hostname}/{entry['filename']}"
                st.write(filename_url)
        else:
            st.error("Failed to extract data from the DS_Store file.")
