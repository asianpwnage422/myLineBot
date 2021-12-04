from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# My Code
from util import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('++7wQ1tXdLomUPrrUbvcKEE12HAh+eeIh1s46ynQESIAH2zkobGXkk19oxFSHS/5fgOju9fHnX3wu02ALT70wQSYcrFuE5ZoKd5vYwkr+VRIdTiMfFSVFerWzr5j1Syf5YlS5NGCFoXbPBiF730F3AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('095348740b93fb668776aa36c9571a44')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '聯絡方式' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '你是誰' in msg:
        message = TextSendMessage(text= "嗨我是吳岳，很高興認識你！")
        line_bot_api.reply_message(event.reply_token, message)
    elif '你會什麼' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '你喜歡什麼' in msg:
        message = image_gallery()
        line_bot_api.reply_message(event.reply_token, message)
    elif "你想去哪裡工作" in msg:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='LINE Taiwan', address='No. 333號, Ruiguang Rd, Neihu District, Taipei City, 114', latitude=25.07726625171245, longitude=121.57513202616131))
    else:
        message = TextSendMessage(text='echo: ' + msg)
        line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
