from flask import Flask, request, abort #create a light website for Linbot connection
import json #read the data from line
import requests #reach the data from internet immediately
import time # get the current time
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, JoinEvent, TextMessage, TextSendMessage)

Line_bot_api = LineBotApi('mGZ+2slcF0VcNjs1YvreNpOm3h4STfJqPUzTonl64akZ79ieFSZjgvHU/PFx44dNBbzfcL5odxlvtcMcDaPeriu2A7LD43fPhkrOHzcS4Y5MSBg6gmto7Jqv15fOuODPKc2NdPWWiR108i0ti4u1VwdB04t89/1O/w1cDnyilFU=') # Linebot customize Api
handler = WebhookHandler('008021c29864de0a406566a9ad5e01de') # channel secret
app = Flask(__name__)

@app.route("/callback", methods = ['POST'])
def callback(): #checking if the input message is right
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text = True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#鸚鵡程式: 測試用
'''@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    Line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))'''

#part1: OAuth for the authenztization
@handler.add(MessageEvent, message=TextMessage)
def first_login(event):
    if :
        creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=5, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    app.run() 