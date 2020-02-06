import urllib.error
from datetime import datetime
from message import GetMessage
from send_message import CreateMessage, SendMessage
from store_dir import FolderName
import codecs


def SendEmail(service, messages):
    sender = 'Managers@seventwopartners.com'
    to = 'Managers@seventwopartners.com'
    time = datetime.now()
    new_ts = time.strftime("%m/%d/%Y")
    subject = f'Email Summary: {new_ts}'

    inserts = HtmlInserts(service, messages)

    f = open("/Email_scrypt/72_gmail-master/quickstart/email_og.html", "r")
    contents = f.readlines()
    f.close()

    contents.insert(267, inserts[0])
    contents.insert(295, inserts[1])
    contents.insert(323, inserts[2])
    contents.insert(351, inserts[3])

    f = open("/Email_scrypt/72_gmail-master/quickstart/email.html", "w", encoding='utf-8')
    contents = "".join(contents)
    f.write(contents)
    f.close()

    f=codecs.open("/Email_scrypt/72_gmail-master/quickstart/email.html", 'r', encoding='utf-8')
    message_text = f.read()
    f.close()
    message = CreateMessage(sender, to, subject, message_text)
    SendMessage(service, 'me', message)


def HtmlInserts(service, messages):
    email_tuple = []
    subject_tuple = []
    folder_tuple = []
    attachment_tuple = []

    for message in messages:
        message_data = GetMessage(service, 'me', message['id'])
        headers = message_data['payload']['headers']
        try:
            email = list(filter(lambda x: 'From' in x['name'], headers)).pop()['value']
            subject = list(filter(lambda x: 'Subject' in x['name'], headers)).pop()['value'][:100]
        except:
            email = "Manager's Email"
            subject = "N/A"

        folder = FolderName(service, message['id'])
        #import pdb; pdb.set_trace()
        #folder = list(filter(lambda folder: folder[0] == message['id'], folder_data)).pop()
        #snippet = message_data['snippet']
        attachment = AttachmentQuerry(message_data['payload'])

        email_tuple.append(f'<p style="font-size: 14px; line-height: 1.2; mso-line-height-alt: 17px; margin: 0; max-height: 150px; min-height: 150px; max-width: 180px; vertical-align: middle">{email}</p>')
        subject_tuple.append(f'<p style="font-size: 14px; line-height: 1.2; mso-line-height-alt: 17px; margin: 0; max-height: 150px; min-height: 150px; max-width: 180px; vertical-align: middle">{subject}</p>')
        folder_tuple.append(f'<p style="font-size: 14px; line-height: 1.2; mso-line-height-alt: 17px; margin: 0; max-height: 150px; min-height: 150px; max-width: 180px; vertical-align: middle">{folder}</p>')
        attachment_tuple.append(f'<p style="font-size: 14px; line-height: 1.2; mso-line-height-alt: 17px; margin: 0; max-height: 150px; min-height: 150px; max-width: 180px; vertical-align: middle">{attachment}</p>')

    email_text = ''.join(email_tuple)
    subject_text = ''.join(subject_tuple)
    folder_text = ''.join(folder_tuple)
    attachment_text = ''.join(attachment_tuple)
    return email_text, subject_text, folder_text, attachment_text


def AttachmentQuerry(payload):
    try:
        parts = [payload]
        while parts:
          part = parts.pop()
          if part.get('parts'):
              parts.extend(part['parts'])
          if part.get('filename'):
              if 'data' in part['body']:
                  return 'Yes'
                  #file_data = base64.urlsafe_b64decode(part['body']['data'].encode('UTF-8'))
                  #self.stdout.write('FileData for %s, %s found! size: %s' % (message['id'], part['filename'], part['size']))
              elif 'attachmentId' in part['body']:
                  #attachment = service.users().messages().attachments().get(
                #      userId=user_id, messageId=message['id'], id=part['body']['attachmentId']
                  #).execute()
                  #file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                  #self.stdout.write('FileData for %s, %s found! size: %s' % (message['id'], part['filename'], attachment['size']))
                  return 'Yes'
              else:
                  return "No"
                  #file_data = None
              # if file_data:
              #     folder_name = FolderName(service, msg_id)
              #     try:
              #         os.mkdir(f'/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/attachments/{folder_name}')
              #         store_dir = f'/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/attachments/{folder_name}/'
              #     except OSError:
              #         store_dir = f'/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/attachments/{folder_name}/'
              #
              #     path = ''.join([store_dir, part['filename']])
              #     with open(path, 'wb') as f:
              #         f.write(file_data)
    except urllib.error.HttpError as e:
      print ('An error occurred: %s' % error)
    else:
        return "No"
