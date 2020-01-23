"""Retrieve an attachment from a Message.
"""

import base64
from apiclient import errors
import urllib.error
from store_dir import FolderName
import os


def GetAttachments(service, user_id, msg_id):
  """Get and store attachment from Message with given id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: ID of Message containing attachment.
    store_dir: The directory used to store attachments.
  """
  try:
      message = service.users().messages().get(userId=user_id, id=msg_id).execute()
      parts = [message['payload']]
      while parts:
        part = parts.pop()
        if part.get('parts'):
            parts.extend(part['parts'])
        if part.get('filename'):
            if 'data' in part['body']:
                file_data = base64.urlsafe_b64decode(part['body']['data'].encode('UTF-8'))
                #self.stdout.write('FileData for %s, %s found! size: %s' % (message['id'], part['filename'], part['size']))
            elif 'attachmentId' in part['body']:
                attachment = service.users().messages().attachments().get(
                    userId=user_id, messageId=message['id'], id=part['body']['attachmentId']
                ).execute()
                file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                #self.stdout.write('FileData for %s, %s found! size: %s' % (message['id'], part['filename'], attachment['size']))
            else:
                file_data = None
            if file_data:
                folder_name = FolderName(service, msg_id)
                try:
                    os.mkdir(f'/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/attachments/{folder_name}')
                    store_dir = f'/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/attachments/{folder_name}/'
                except OSError:
                    store_dir = f'/Users/hlevin/SevenTwoPartners/gmail_py/quickstart/attachments/{folder_name}/'

                path = ''.join([store_dir, part['filename']])
                with open(path, 'wb') as f:
                    f.write(file_data)
  except urllib.error.HttpError as e:
    print ('An error occurred: %s' % error)
