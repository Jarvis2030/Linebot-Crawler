# Linebot-Crawler
## Overview
Restaurant recommendation system using LINEbot as deploy platform

## Get Started
---------------------------------
This is an ongoing project and will be continuously updated in the future. However if you will like to download and get started, follow the step below:
1. Run the code below to start the local server:
```
git clone https://github.com/Jarvis2030/Linebot-Crawler.git
python app.py
ngrok http 5000
```
2. Set the access token and secret to your own one in config.ini
```
[line-bot]
channel_access_token = 'your access token'
channel_secret = 'your secret'
```
3. setup the webhook using the with ngrok public address
<img width="1162" alt="截圖 2023-09-30 下午10 49 35" src="https://github.com/Jarvis2030/Linebot-Crawler/assets/77675271/4ca092b7-e705-4959-941a-ae1d225b6e6c">
4. test the connection with the 'verify' button

## Debugging
---------------------------------
1. If there is any connection error, you can clink into the web interface to see the error code.
2. Make sure you are using the right route in the Line webhook.

