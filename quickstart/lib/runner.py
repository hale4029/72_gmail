""" retreive attachments and save in folder """
#from labels import *
from list import ListMessagesMatchingQuery
from time_stamp import *
#from message import *
from quickstart import main
from attachment import GetAttachments
#import os

service = main()
time_stamp = PreviousTimeStamp()
query = f'from: harrison.levin@colorado.edu, after: {time_stamp}'
max_results = 10
user_id = 'me'
store_dir = '/Users/hlevin/SevenTwoPartners/gmail_py/'

message_list = ListMessagesMatchingQuery(service, user_id, query, max_results)

for id in message_list:
   GetAttachments(service, user_id, id['id'], store_dir)

UpdateTimeStamp()
