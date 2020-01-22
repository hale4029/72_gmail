from quickstart import main

service = main()

# Call the Gmail API
results = service.users().labels().list(userId='me').execute()
labels = results.get('labels', [])

# if not labels:
#     print('No labels found.')
# else:
#     print('Labels:')
#     for label in labels:
#         print(label['name'])
#
# if __name__ == '__main__':
#     main()
