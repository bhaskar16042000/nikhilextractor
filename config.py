"""
from os import getenv


API_ID = int(getenv("API_ID", "27567486"))
API_HASH = getenv("API_HASH", "b1760d4b5ef697bb8da4e7ac4e261c49")
BOT_TOKEN = getenv("BOT_TOKEN", "8205655735:AAFylt5DAsP3aD8VnB1VGmLYLJn31HS4gPU")
OWNER_ID = int(getenv("OWNER_ID", "7780806801"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7780806801,7780806801").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://cap16042000:Dii1XxrhxtKge5EA@cluster0.avgkact.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002976364859"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002934210120"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27567486"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "b1760d4b5ef697bb8da4e7ac4e261c49")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8205655735:AAFylt5DAsP3aD8VnB1VGmLYLJn31HS4gPU")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Nikhilextractor_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7780806801"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7780806801,7780806801").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002656120306"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://cap16042000:Dii1XxrhxtKge5EA@cluster0.avgkact.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002934210120"))

