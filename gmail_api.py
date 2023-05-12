from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64


class GmailAPI:
    def __init__(self):
        # Build service
        creds = Credentials.from_authorized_user_file("credentials.json", ['https://www.googleapis.com/auth/gmail.modify'])
        self.service = build('gmail', 'v1', credentials=creds)

    def get_last_unread_message(self):
        # get the list of unread messages
        results = self.service.users().messages().list(userId='me', q='is:unread').execute()

        # get the id of the last unread message
        if 'messages' in results:
            last_message_id = results['messages'][-1]['id']

            # get the last unread message
            last_message = self.service.users().messages().get(userId='me', id=last_message_id).execute()

            # mark the message as read
            try:
                self.service.users().messages().modify(
                    userId='me', id=last_message_id, body={'removeLabelIds': ['UNREAD'], 'addLabelIds': ['INBOX']}).execute()
            except HttpError as error:
                print('An error occurred: %s' % error)
                
            # get the message body
            message_parts = last_message['payload']['parts']
            if not message_parts:
                message_body = base64.urlsafe_b64decode(last_message['payload']['body']['data']).decode('utf-8')
            else:
                message_body = ''
                for part in message_parts:
                    if part['mimeType'] == 'text/plain':
                        message_body += base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                        
            # get the sender email address
            sender = ''
            for header in last_message['payload']['headers']:
                if header['name'] == 'From':
                    sender = header['value']
                    break
            
            # return the sender, message subject, and body text
            return sender, last_message['payload']['headers'][15]['value'], message_body

        else:
            return None