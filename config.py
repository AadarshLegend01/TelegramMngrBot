import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "3244057")
    API_HASH = getenv("API_HASH", "b8a814ed15eada43bc8c86d89d7f7618")
    TOKEN = getenv("TOKEN", "5530982980:AAFikeFIdiwef5QVxG0A5kX22iNKHJ4YhFc")
    OWNER_ID = getenv("3244057")
    STRING_SESSION = getenv("BQBLqQiw9-XpMHCa7LKoqDnzr_Rsh6tGKs49yBrigItZv1THjI1e65G8FZG6T4b8kSIOV4NsYfZNPZR_Is-JM8pG4cszzsqku83XCAx0ZjCd8C_fEuSHXmLeAi5A8_0fM285m5JjiBkiGczPH_kCgwkl7Oo8ck7qPhSPR_1hE4juwqGEskTSMlIDlc1-Xv0HN2cgIOfjYGdJeb8rb4q3Cj0jsCn03pZc_wYVJ0X0uiL9KCOGiBCyH5tLVKbg4L6OVbvWYz3Y4LuYVco2LlJRQya9_Phkkt0xENsx5AdaLUtJYCTQa1NUspYQ85yXXudBqPbMOITPN6cY8FJ2b8CKk67URLwAUAA", "")
    OWNER_USERNAME = getenv("Aadarsh_Legend", "")
    DB_URI = getenv("DATABASE_URL", "")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001509525202")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001509525202")
    SYS_ADMIN = getenv("SYS_ADMIN", "1669178360")
    DEV_USERS = getenv("DEV_USERS", "1669178360")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
