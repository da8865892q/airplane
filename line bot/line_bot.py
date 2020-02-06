# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from six.moves import configparser

app = Flask(__name__)

# LINEBOT 基本資料
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 接收 LINE 的訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "航空機場":
        line_bot_api.reply_message(
            event.reply_token,
            ImagemapSendMessage(
                base_url='https://i.imgur.com/04yxkDA.png',
                alt_text='航空公司與機場查詢',
                base_size=BaseSize(height=350, width=1040),
                actions=[
                    URIImagemapAction(      # 查詢所有機場資訊
                        link_uri='line://app/1611671390-32NYP0mW',
                        area=ImagemapArea(
                            x=0, y=0, width=1040, height=350
                        )
                    ),
                    URIImagemapAction(      # 查詢航空公司資訊
                        link_uri='line://app/1611671390-E54MRWKp',
                        area=ImagemapArea(
                            x=520, y=0, width=1040, height=350
                        )
                    )
                ]
            )
        )
    elif event.message.text == "航班時刻":
        line_bot_api.reply_message(
            event.reply_token,
            ImagemapSendMessage(
                base_url='https://i.imgur.com/LTvzz0q.png',
                alt_text='航班與時刻表查詢',
                base_size=BaseSize(height=350, width=1040),
                actions=[
                    URIImagemapAction(      # 查詢即時航班資料
                        link_uri='line://app/1611671390-Opq9edmn',
                        area=ImagemapArea(
                            x=0, y=0, width=1040, height=350
                        )
                    ),
                    URIImagemapAction(      # 查詢定期時刻表
                        link_uri='line://app/1611671390-VKq07rxm',
                        area=ImagemapArea(
                            x=520, y=0, width=1040, height=350
                        )
                    )
                ]
            )
        )
    elif event.message.text == "關於我們":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="facebook: https://www.facebook.com/\n\ninstagram: https://www.instagram.com/"
            )
        )
    elif event.message.text == "使用說明":
        line_bot_api.reply_message(
            event.reply_token,
            VideoSendMessage(
                original_content_url='https://i.imgur.com/eRwALTN.mp4',
                preview_image_url='https://i.imgur.com/tWD5q3l.png'
            )
        )

if __name__ == "__main__":
    app.run()
