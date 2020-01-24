import urllib.error
from datetime import datetime
from message import GetMessage
from send_message import CreateMessage, SendMessage
import codecs


def SendEmail(service, messages):
    sender = 'harrison483@gmail.com'
    to = 'harrison483@gmail.com'
    time = datetime.now()
    new_ts = time.strftime("%m/%d/%Y")
    subject = f'Email Summary: {new_ts}'

    inserts = HtmlInserts(service, messages)

    f = open("/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/email_og.html", "r")
    contents = f.readlines()
    f.close()

    contents.insert(265, inserts[0])
    contents.insert(285, inserts[1])
    contents.insert(307, inserts[2])

    f = open("/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/email.html", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

    f=codecs.open("/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/email.html", 'r')
    message_text = f.read()
    f.close()
    message = CreateMessage(sender, to, subject, message_text)
    SendMessage(service, 'me', message)


def HtmlInserts(service, messages):
    email_tuple = []
    snippet_tuple = []
    attachment_tuple = []

    for message in messages:
        message_data = GetMessage(service, 'me', message['id'])
        headers = message_data['payload']['headers']
        email = list(filter(lambda x: 'From' in x['name'], headers)).pop()['value']
        snippet = message_data['snippet']
        attachment = AttachmentQuerry(message_data['payload'])

        email_tuple.append(f'{email}<br>')
        snippet_tuple.append(f'{snippet}<br>')
        attachment_tuple.append(f'{attachment}<br>')

    email_text = ''.join(email_tuple)
    snippet_text = ''.join(snippet_tuple)
    attachment_text = ''.join(attachment_tuple)
    return email_text, snippet_text, attachment_text


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
