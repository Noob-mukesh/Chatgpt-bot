from config import *
import logging

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client


logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

LOGGER = logging.getLogger(__name__)

mongo = MongoCli(DATABASE_URI)
db = mongo.chatgpt


class Mukesh(Client):
    def __init__(self):
        super().__init__(
            name="Chatgpt",
            api_id=API_ID,
            api_hash=API_HASH,
            lang_code="en",
            bot_token=BOT_TOKEN,
            in_memory=True,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()


Mukesh = Mukesh()