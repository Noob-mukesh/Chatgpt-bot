import os
API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "mr_sukkun")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "the_support_chat")
START_IMG = os.environ.get(
    "START_IMG", "https://graph.org/file/d4412c7b411ca8da9e177.jpg"
)

MONGO_DB_URI = os.environ.get(
    "MONGO_DB_URI",
    "",
)
DATABASE_URI=MONGO_DB_URI
OWNER_ID=6728038801
