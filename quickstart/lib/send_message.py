"""Send an email message from the user's account.
"""

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
import urllib.error
from apiclient import errors

from quickstart import main
from attachment import GetAttachments
from message import GetMessage
from message_parts import AttachmentQuerry


def SendMessage(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())

    return message
  except urllib.error.HttpError as e:
    print('An error occurred: %s' % error)


def CreateMessage(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
  b64_string = b64_bytes.decode()
  body = {'raw': b64_string}
  return body



service = main()
sender = 'harrison483@gmail.com'
to = 'harrison483@gmail.com'
subject = 'Email Summary'

message = GetMessage(service, 'me', '16fca5736f94c25b')
headers = message['payload']['headers']

email = list(filter(lambda x: 'From' in x['name'], headers)).pop()['value']
snippet = message['snippet']
attachment = AttachmentQuerry(message['payload'])

message_text = f'From: {email}    Snippet: {snippet}    Attachment: {attachment}'

message = CreateMessage(sender, to, subject, message_text)
SendMessage(service, 'me', message)
