

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
credentials = None

# token.pickle stores the user's credentials from previously successful logins
if os.path.exists('token.pickle'):
    print('Loading Credentials From File...')
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

# If there are no valid credentials available, then either refresh the token or log in.
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        print('Fetching New Tokens...')
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json',
            scopes=[
                'https://www.googleapis.com/auth/youtube.force-ssl'
            ]
        )

        flow.run_local_server(port=8080, prompt='consent',
                              authorization_prompt_message='')
        credentials = flow.credentials

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as f:
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)
            
youtube = build('youtube','v3', credentials=credentials)

request_body = {
    'snippet': {
        'videoId':'qboVz60LupQ',
        'topLevelComment': {
            
            'snippet':  {
                
                'textOriginal':'Hello 9999'
                }
            
            }
        
        
        }
    
    }
            
request = youtube.commentThreads().insert(
    part='snippet',
    body=request_body
)
response = request.execute()

print(response)         
            

