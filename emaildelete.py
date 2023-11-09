import imaplib

# IMAP server settings
imap_server = "imap.gmail.com"
imap_port = 993
username = "email@gmail.com"
app_password = "yourpassword"

# Keyword to filter emails
keyword = "changekeyword"

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(imap_server, imap_port)

try:
    # Log in to your email account
    mail.login(username, app_password)

    # Select the mailbox (e.g., INBOX)
    mailbox = "INBOX"
    mail.select(mailbox)

    # Search for emails that contain the keyword
    search_query = f'NOT (TEXT "{keyword}")'
    status, email_ids = mail.search(None, search_query)

    if status == 'OK':
        email_id_list = email_ids[0].split()
        
        # Iterate over the email IDs and delete them
        for email_id in email_id_list:
            mail.store(email_id, '+FLAGS', '(\Deleted)')
        
        # Expunge to permanently delete the marked emails
        mail.expunge()
        
        print(f"Deleted {len(email_id_list)} emails without containing the keyword '{keyword}'")
    else:
        print("Failed to search for emails.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Logout and close the connection
    mail.logout()
