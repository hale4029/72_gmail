#from quickstart import main
from message import GetMessage
import numpy as np

# service = main()
# msg_id = '16fd3813f0ad7990'
# user_id = 'me'

def FolderName(service, msg_id):
    '''previously created labels in GMAIL'''
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels')

    ''' message info '''
    message = GetMessage(service, 'me', msg_id)

    ''' assign to gmail folder '''
    try:
        label_id= message['labelIds'][1]
        folder_name = list(filter(lambda label: label['id'] == label_id, labels))[0]['name']
        return folder_name
    except:
         return 'unassigned'
