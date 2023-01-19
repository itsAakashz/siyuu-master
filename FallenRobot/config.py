class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 11457698
    API_HASH = "5bfd698491bd1a495c2acd0842c65b90"

    CASH_API_KEY = " 8DIIPVROWD8S2CLJ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://dphmkvgr:DeTfgdB47uBW4_wpDDOcTc1PxBYejtXE@tiny.db.elephantsql.com/dphmkvgr"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001683658964)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://ItsAakashz:<Aakash7>@cluster0.ny2gony.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = " https://te.legra.ph/file/f5fd6e9c08624ffbe9d6a.jpg"

    SUPPORT_CHAT = "Fun_talks"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5504112672:AAHfAWjMla0-FDj-loycLddPCtgOrzC_82c"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "OJDD3DCONB4W"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1097379245  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1097379245]  # User id of sudo users
    DEV_USERS = [1097379245]  # User id of dev users
    DEMONS = [1097379245]  # User id of support users
    TIGERS = [1097379245]  # User id of tiger users
    WOLVES = [1097379245]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
