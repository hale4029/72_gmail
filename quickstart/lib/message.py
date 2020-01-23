from quickstart import main
import base64
import email
import urllib.error
from apiclient import errors

service = main()
msg_id = '16fca5736f94c25b'
user_id = 'me'

def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    print ('Message snippet: %s' % message['snippet'])

    return message
  except urllib.error.HttpError as e:
    print ('An error occurred: %s' % error)


def GetMimeMessage(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    print('Message snippet: %s' % message['snippet'])

    msg_str = str(base64.urlsafe_b64decode(message['raw'].encode('ASCII')),'UTF-8')

    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except urllib.error.HttpError as e:
    print ('An error occurred: %s' % error)
