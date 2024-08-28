# (c) adarsh-goel
import os
import sys
from os import getenv, environ
from dotenv import load_dotenv


load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv("API_ID", "10115546"))
    API_HASH = str(getenv("API_HASH", "366347107f54aabc951cfa9d3c2fb2ce"))
    BOT_TOKEN = str(getenv("BOT_TOKEN", "7281537410:AAHsQ3joGTZvgbTFA7uj1oqaGy_4KM3fmsI"))
    name = str(getenv("name", "filetolinkbot"))
    SLEEP_THRESHOLD = int(getenv("SLEEP_THRESHOLD", "60"))
    WORKERS = int(getenv("WORKERS", "4"))
    BIN_CHANNEL = int(getenv("BIN_CHANNEL", "-1001690683283"))
    PORT = int(getenv("PORT", 8080))
    BIND_ADRESS = str(getenv("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1358956715").split())
    NO_PORT = bool(getenv("NO_PORT", False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv("OWNER_USERNAME", "ownerimmanvpn"))
    HASH_LENGTH = int(environ.get("HASH_LENGTH", 6))
    if not 5 < HASH_LENGTH < 64:
        sys.exit("Hash length should be greater than 5 and less than 64")
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv("APP_NAME"))

    else:
        ON_HEROKU = False
    FQDN = str(getenv("FQDN", BIND_ADRESS)) if not ON_HEROKU or getenv("FQDN") else APP_NAME + ".herokuapp.com"
    HAS_SSL = bool(getenv("HAS_SSL", False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv("DATABASE_URL", "mongodb+srv://iteasy05:AS2ftxVxjQSWkQbE@cluster0.chw2i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    UPDATES_CHANNEL = str(getenv("UPDATES_CHANNEL", None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
