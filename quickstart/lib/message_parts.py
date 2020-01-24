import urllib.error

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


    #
    # parts = [payload]
    # part = parts.pop()
    # import pdb; pdb.set_trace()
    # # if part.get('parts'):
    # #   parts.extend(part['parts'])
    # if part.get('filename'):
    #   if 'data' in part['body']:
    #       return 'Yes'
    #   elif 'attachmentId' in part['body']:
    #       return 'Yes'
    #   else:
    #       return 'No'
