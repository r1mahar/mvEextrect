import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "8009092037:AAGmJO7YG3jlzwV3c2R6lO5eP4BWWcXCws8"
    # Telegram API ki ID
    API_ID = 25773625
    # Telegram API ki hash key
    API_HASH = "137dc2742789fc81191a9bf7a25ff922"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '6960427846,5548106944,7421218284,7385324642'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://username:password@cluster0.example.mongodb.net/?retryWrites=true&w=majority"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002298028655
    # Authentication log channel ki ID
    AUTH_LOG = -1002422315021
    # Hit log channel ki ID
    HIT_LOG = -1002445568877
    # DRM dump channel ki ID
    DRM_DUMP = -1002272364872
    # Main channel ki ID
    CHANNEL = -1002405481282
    # Channel ka link
    CH_URL = "https://t.me/+MqrT6AsUKjNkY2Nl"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/Gp1804"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://drm-api-five.vercel.app"

