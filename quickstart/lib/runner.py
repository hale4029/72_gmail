""" retreive attachments and save in folder """
from list import ListMessagesMatchingQuery
from time_stamp import *
from quickstart import main
from attachment import GetAttachments
from message_parts import SendEmail
import os

service = main()
time_stamp = PreviousTimeStamp()
query = f'from: -managers@seventwopartners.com, after: {time_stamp}'
max_results = None
user_id = 'me'

message_list = ListMessagesMatchingQuery(service, user_id, query, max_results)

# #folder_collection =[]
for id in message_list:
    GetAttachments(service, user_id, id['id'])
#    #folder_collection.append(GetAttachments(service, user_id, id['id']))
#   # import pdb; pdb.set_trace()

SendEmail(service, message_list)

os.remove("../email.html")

UpdateTimeStamp()
