import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7550452226:AAHmHKpLAElQNAqNIJnxrj8_Mfm339o3cL4"
    # Telegram API ki ID
    API_ID = 25773625
    # Telegram API ki hash key
    API_HASH = "137dc2742789fc81191a9bf7a25ff922"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '7385324642'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://mewadonlinestudy:yYjxKiZGQag8DnWH@cpvod.ywpecvo.mongodb.net/?retryWrites=true&w=majority&appName=cpvodak"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002470171280
    # Authentication log channel ki ID
    AUTH_LOG = -1002470171280
    # Hit log channel ki ID
    HIT_LOG = -1002470171280
    # DRM dump channel ki ID
    DRM_DUMP = -1002470171280
    # Main channel ki ID
    CHANNEL = -1002470171280
    # Channel ka link
    CH_URL = "https://t.me/+sYOgy9ZgCZRhYTNl"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/Ganshyamv"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "www.masterapi.tech"

