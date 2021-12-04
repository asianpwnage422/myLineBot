#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/TM8Of0L.png",
        alt_text='聯絡方式',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #LinkedIn
                link_uri="https://www.linkedin.com/in/kevin-wu-22427117b/",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #Instagram
                link_uri="https://www.instagram.com/w.yueh_ark4/",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #Facebook
                link_uri="https://www.facebook.com/theYueh",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #Twitter
                link_uri="https://twitter.com/TheYueh",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=1000
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面
#TO-DO
def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png',
                    title='Python',
                    text='Click Below!',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='能力值',
                            text='⭐️⭐️⭐️'
                        ),
                        URITemplateAction(
                            label='Website',
                            uri='https://www.python.org/'
                        )
                    ]
                ),
               CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/8/88/Java_logo.png',
                    title='Java',
                    text='Click Below!',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='能力值',
                            text='⭐️⭐️⭐️⭐️'
                        ),
                        URITemplateAction(
                            label='Past Project',
                            uri='https://play.google.com/store/apps/details?id=poorni.bamboo_new'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png',
                    title='JavaScript',
                    text='Click Below!',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='能力值',
                            text='⭐️⭐️⭐️'
                        ),
                        URITemplateAction(
                            label='Past Projects',
                            uri='https://github.com/asianpwnage422/JavaScript-Projects'
                        )
                    ]
                ),
            ]
        )
    )
    return message

def image_gallery():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://media.istockphoto.com/photos/happy-coffee-cup-picture-id508347326?k=20&m=508347326&s=612x612&w=0&h=phdf_0eKqIbCj2ayXuXRktf8JGugJqFXdi6A8gBL6vU=",
                    action=URITemplateAction(
                        label="Coffee",
                        uri="https://media.istockphoto.com/photos/happy-coffee-cup-picture-id508347326?k=20&m=508347326&s=612x612&w=0&h=phdf_0eKqIbCj2ayXuXRktf8JGugJqFXdi6A8gBL6vU="
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://cdn.dribbble.com/users/1931394/screenshots/9780708/image.png",
                    action=URITemplateAction(
                        label="Music",
                        uri="https://cdn.dribbble.com/users/1931394/screenshots/9780708/image.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="Dogs",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="Cats",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message