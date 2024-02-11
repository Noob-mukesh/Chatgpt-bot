
# #-----------CREDITS -----------
# # telegram : @legend_coder
# # github : noob-mukesh
# from pyrogram import Client, filters,enums,idle
# from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
# from pyrogram.enums import ChatAction, ParseMode

# from pyrogram.types import CallbackQuery
# from config import *
# import os,sys,re,requests
# import asyncio,time
# from random import choice
# from bardapi import Bard
# from datetime import datetime
# import logging

# FORMAT = "[LEGEND-MUKESH] %(message)s"
# logging.basicConfig(
#     level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )


# StartTime = time.time()
# Mukesh = Client(
#     "chat-gpt" ,
#     api_id = API_ID,
#     api_hash = API_HASH ,
#     bot_token = BOT_TOKEN
# )


  
# #         start
# @Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
# async def start(client, m: Message):
#     try:
#         accha = await m.reply_text(
#                         text = f"{g}")
#         await asyncio.sleep(0.2)
#         await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
#         await asyncio.sleep(0.2)
#         await accha.delete()
#         umm = await m.reply_sticker(
#                   sticker = STKR,
#         )
#         await asyncio.sleep(0.3)
#         await umm.delete()
#         await m.reply_photo(
#             photo = START_IMG,
#             caption=START,
#             reply_markup=InlineKeyboardMarkup(MAIN),
#         )
#     except Exception as y:
#         await m.reply(y)
# #  callback 
# @Mukesh.on_callback_query()
# async def cb_handler(Client, query: CallbackQuery):
#     if query.data == "HELP":
#      await query.message.edit_text(
#                       text = HELP_READ,
#                       reply_markup = InlineKeyboardMarkup(HELP_BACK),
#      )
#     elif query.data == "HELP_BACK":
#             await query.message.edit(text = START,
#                   reply_markup=InlineKeyboardMarkup(MAIN),
#         )
    
# @Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
# async def restart(client, message):
#     hmm = await message.reply_photo(START_IMG,
#                         caption=HELP_READ,
#                         reply_markup= InlineKeyboardMarkup(HELP_BACK),
#        )
# @Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
# async def source(bot, m):
    
#     await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
# #  alive
# @Mukesh.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
# async def ping(client, message: Message):
#         start = datetime.now()
#         t = "ριиgιиg..."
#         txxt = await message.reply(t)
#         await asyncio.sleep(0.25)
#         await txxt.edit_text("ριиgιиg.....")
#         await asyncio.sleep(0.35)
#         await txxt.delete()
#         end = datetime.now()
#         ms = (end-start).microseconds / 1000
#         await message.reply_photo(
#                              photo=START_IMG,
#                              caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [ᴍᴜᴋᴇsʜ](https://t.me/legend_coder)||",
#                              reply_markup=InlineKeyboardMarkup(PNG_BTN),
#        )

# #  main   

# @Mukesh.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
# async def chat(bot, message):
    
#     try:
#         start_time = time.time()
#         await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
#         if len(message.command) < 2:
#             await message.reply_text(
#             "Example:**\n\n`/chatgpt Where is TajMahal?`")
#         else:
#             a = message.text.split(' ', 1)[1]
#             response = requests.get(f'https://mukesh-api.vercel.app/chatgpt?query={a}') 
#             x=response.json()["results"]
#             end_time = time.time()
#             telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
#             await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
#     except Exception as e:
#         await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")

# #  bard 

# @Mukesh.on_message(filters.command(["bard"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
# async def chat(bot, message):
    
#     try:
#         start_time = time.time()
#         await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
#         if len(message.command) < 2:
#             await message.reply_text(
#             "Example:**\n\n`/bard Where is TajMahal?`")
#         else:
#             a = message.text.split(' ', 1)[1]
#             response = requests.get(f'https://mukesh-api.vercel.app/bard?query={a}') 
#             x=response.json()["results"]
#             end_time = time.time()
#             telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
#             await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
#     except Exception as e:
#         await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
    
# #  blackbox

# @Mukesh.on_message(filters.command(["blackbox"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
# async def chat(bot, message):
    
#     try:
#         start_time = time.time()
#         await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
#         if len(message.command) < 2:
#             await message.reply_text(
#             "Example:**\n\n`/blackbox Where is TajMahal?`")
#         else:
#             a = message.text.split(' ', 1)[1]
#             response = requests.get(f'https://mukesh-api.vercel.app/blackbox?query={a}') 
#             x=response.json()["results"]
#             end_time = time.time()
#             telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
#             await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
#     except Exception as e:
#         await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
# s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()

# if SOURCE != s:
#     print("So sad, you have changed source, change it back to ` https://github.com/Noob-mukesh/Chatgpt-bot `  else I won't work")
#     sys.exit(1)  


# if __name__ == "__main__":
#     print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
#     """)
#     try:
#         Mukesh.start()
        
        
#     except (ApiIdInvalid, ApiIdPublishedFlood):
#         raise Exception("Your API_ID/API_HASH is not valid.")
#     except AccessTokenInvalid:
#         raise Exception("Your BOT_TOKEN is not valid.")
#     print(f"""JOIN  @MR_SUKKUN
# GIVE STAR TO THE REPO 
#  {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
#     """)
#     idle()
#     Mukesh.stop()
#     print("Bot stopped. Bye !")
# #-----------CREDITS -----------
# # telegram : @legend_coder
# # github : noob-mukesh
