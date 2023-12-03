import datetime
from get_context import *
import imaplib
import ssl
import pickle

def get_number_unread_emails()->int:
    # Connect to Gmail IMAP server

    custom_port = 2143  # Change this to your custom port number
    mail = imaplib.IMAP4('127.0.0.1', custom_port)
    # Start TLS to upgrade the connection to a secure one
    mail.starttls()

    # Login to your account
    username = 'romain.mendez@protonmail.com'
    password = 'Wx9szu7PmzLgW4pc_0wgxA'
    mail.login(username, password)

    # Select the mailbox you want to check (e.g., 'INBOX')
    mail.select('INBOX')

    # Search for unseen emails
    status, response = mail.search(None, 'UNSEEN')
    
    # Get the list of unseen emails
    unseen_emails = len(response[0].decode(encoding="utf-8").split(" "))

    if unseen_emails != 0:
        print(f"You have {unseen_emails} unseen emails!")
        # Process or fetch these emails if needed
        # this is some comment

    # Logout from the server
    mail.logout()
    return unseen_emails

def trigger_thunderbird(trigger_time = datetime.timedelta(seconds=15))->bool:
    def load_integer_from_pickle(file_path: str) -> int:
        with open(file_path, 'rb') as file:
            integer = pickle.load(file)
        return integer
    
    unread_emails = get_number_unread_emails()
    
    try:
        last_number_of_emails_unseen = load_integer_from_pickle("./last_time_on_thunderbird.pickle")
    except:
        with open("./last_time_on_thunderbird.pickle", 'wb') as file:
            pickle.dump(unread_emails, file)
        last_number_of_emails_unseen = load_integer_from_pickle("./last_time_on_thunderbird.pickle")
    

    #Check when was the last time you were on Thunderbird
    last_time_on = get_last_time_on("thunderbird_mail")
    
    #Check if at least one unread 


    if last_time_on > trigger_time:
        if unread_emails > last_number_of_emails_unseen:
            return True
    else: 
        return False


def trigger_pause_reminder(trigger_time = datetime.timedelta(seconds=60))->bool:

    last_pause = get_last_pause()
    print("-----")
    print(last_pause)
    print(last_pause > trigger_time)
    if last_pause is None:
        return False

    if last_pause > trigger_time:
        return True
    else:
        return False