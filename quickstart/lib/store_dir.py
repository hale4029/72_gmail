#from quickstart import main
from message import GetMessage
import numpy as np

#service = main()
#msg_id = '16fd3813f0ad7990'

def FolderName(service, msg_id):
    '''previously created labels in GMAIL'''
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels')

    ''' message info '''
    message = GetMessage(service, 'me', msg_id)

    ''' assign to gmail folder '''
    try:
        message_labels = message['labelIds']
        label_id = list(filter(lambda x: 'Label' in x, message_labels)).pop()
        #label_id= message['labelIds'][1]
        #import pdb; pdb.set_trace()
        folder_name = list(filter(lambda label: label['id'] == label_id, labels)).pop()
        return folder_name['name']
    except:
         return '_unassigned'

#FolderName(service, msg_id)