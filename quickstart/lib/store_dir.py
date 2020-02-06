from message import GetMessage
import numpy as np

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
        folder_name = list(filter(lambda label: label['id'] == label_id, labels)).pop()
        return folder_name['name']
        #return [message['id'], folder_name['name']]
    except:
         return '_unassigned'
