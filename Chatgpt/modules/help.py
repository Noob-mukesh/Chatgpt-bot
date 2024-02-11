# -----------CREDITS -----------
# telegram : @mr_sukkun
# github : noob-mukesh
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup

from .. import Mukesh
from ..modules.buttons import *

@Mukesh.on_message(
    filters.command(
        ["help", f"help@{Mukesh.username}"], prefixes=["+", ".", "/", "-", "?", "$"]
    )
)
async def help(_, m):
    await m.reply_photo(
        START_IMG,
        caption=f"{HELP}",
        reply_markup=InlineKeyboardMarkup(HELP_BACK),quote=True
    )