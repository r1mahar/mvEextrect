import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7687814128:AAE9Dcl_mf8NSEMJgd54dOEL51_M23LePvk"
    # Telegram API ki ID
    API_ID = 24037760
    # Telegram API ki hash key
    API_HASH = "dccc3070f1c12ab155011f14c3d6ae6a"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '7621154046'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://mpsystem05:<db_password>@cluster0.eppygqi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002167527393
    # Authentication log channel ki ID
    AUTH_LOG = -1002578737957
    # Hit log channel ki ID
    HIT_LOG = -1002578737957
    # DRM dump channel ki ID
    DRM_DUMP = -1002578737957
    # Main channel ki ID
    CHANNEL = -1002578737957
    # Channel ka link
    CH_URL = "https://t.me/karma_batch_rwa_2026"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/Final_piece"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

