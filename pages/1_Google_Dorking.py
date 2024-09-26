import streamlit as st

# Set up the page
st.title("Google Dorking Query Generator")
st.write("Enter a hostname to generate Google Dork queries:")

# Input for hostname
hostname = st.text_input("Hostname", "")

# Generate Google Dork queries
if hostname:
    st.write("### Google Dork Queries")
    
    # List of Google Dorking patterns
    
    generic_dork_queries = {
        "Directory_Listing": f"site:{hostname} intitle:index.of",
        "Config_Files": f"site:{hostname} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini",
        "Database_Files": f"site:{hostname} ext:sql | ext:dbf | ext:mdb",
        "WordPress": f"site:{hostname} inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download",
        "Logs": f"site:{hostname} ext:log",
        "Backup_Files": f"site:{hostname} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
        "Login_Pages": f"site:{hostname} inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth",
        "SQL_Errors": f"site:{hostname} intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\"",
        "Document_Files": f"site:{hostname} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv",
        "PHP_Info": f"site:{hostname} ext:php intitle:phpinfo 'published by the PHP Group'",
        "Shell_Backdoor": f"site:{hostname} inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor",
        "URL_Redirects": f"site:{hostname} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http",
        "Code_Sharing_Sites": f"site:http://ideone.com | site:http://codebeautify.org | site:http://codeshare.io | site:http://codepen.io | site:http://repl.it | site:http://justpaste.it | site:http://pastebin.com | site:http://jsfiddle.net | site:http://trello.com | site:*.atlassian.net | site:bitbucket.org \"{hostname}\"",
        "Pastebin_References": f"site:pastebin.com \"{hostname}\"",
        "WordPress_Content": f"site:{hostname} inurl:wp-content | inurl:wp-includes",
        "Bitbucket_Atlassian": f"site:atlassian.net | site:bitbucket.org \"{hostname}\"",
        "StackOverflow_References": f"site:stackoverflow.com \"{hostname}\"",
        "Git_Repositories": f"inurl:\"/.git \"{hostname} -github\"",
        "SWF_Files": f"inurl:{hostname} ext:swf",
        "Amazon_S3_Buckets": f"site:.s3.amazonaws.com \"{hostname}\"",
        "Shodan_Results": f"www.shodan.io/search?query={hostname}",
        "WSDL_Files": f"site:{hostname} filetype:wsdl | filetype:WSDL | ext:svc | inurl:wsdl | Filetype: ?wsdl | inurl:asmx?wsdl | inurl:jws?wsdl | intitle:_vti_bin/sites.asmx?wsdl | inurl:_vti_bin/sites.asmx?wsdl",
        "GitHub_Gists": f"gist.github.com/search?q=*.\"{hostname}\"",
        "Apache_Config": f"site:{hostname} filetype:config \"apache\"",
        "Readme_And_License_Files": f"site:{hostname} inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config",
        "Struts_Action_Files": f"site:{hostname} ext:action | ext:struts | ext:do",
        "PHP_Info_And_Htaccess": f"site:{hostname} inurl:\"/phpinfo.php\" | inurl:\".htaccess\"",
        "Security_Headers_Check": f"securityheaders.com/?q={hostname}&followRedirects=on",
        "Public_Code_Search": f"publicwww.com/websites/\"{hostname}\"/",
        "GitHub_And_GitLab_Repos": f"site:github.com | site:gitlab.com \"{hostname}\"",
        "Subdomains": f"site:*.{hostname} -site:www.{hostname}",
        "Deep_Subdomains": f"site:*.*.{hostname}",
        "Personal_Info_Forms": f"site:{hostname} intext:\"first name\" | intext:firstname | intext:submit | intext:contact | intext:\"Is this article helpful\" | intext:feedback | intext:\"Demo Request\"",
        "Submission_Forms": f"site:{hostname} intitle:submit | intitle:contact | intitle:submit | intitle:feedback | intitle:survey | intitle:form | intitle:\"fill up\"",
        "Feedback_And_Surveys": f"site:{hostname} inurl:contact | inurl:feedback | inurl:survey | inurl:form",
        "Signup_Pages": f"site:{hostname} intitle:signup | intitle:register | intext:signup | intext:\"sign up\" | intext:register | intext:username | inurl:signup | inurl:register",
        "Contact_Us_Pages": f"site:{hostname} intitle:contact | intext:\"contact us\" | intext:survey | intitle:survey",
    }

    # Display the Google Dork queries
    # Generate and display clickable links
    for key, values in generic_dork_queries.items():
        google_search_url = f"https://www.google.com/search?q={values.replace(' ', '+')}"
        st.markdown(f"[{key}]({google_search_url})")
else:
    st.warning("Please enter a hostname to generate the queries.")