from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime
#from database.users_chats_db import db

API_ID = "25450075"
API_HASH = "278e22b00d6dd565c837405eda49e6f2"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = os.environ.get("DATABASE_NAME") 
BOT_USERNAME = os.environ.get("BOT_USERNAME")
BOT_NAME = os.environ.get("BOT_NAME")
ADMINS = os.environ.get("ADMINS")

bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


EMOJIOS = [ 
      "🌿",
      "⚡",
]
      
START = f"""
**๏ Hie Baby🐒 ๏**
"""

@bot.on_message(filters.command("start"))
async def start(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        buttons = [
                  [
                   InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/MUSICBOT_OWNER"),
                   InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/BWF_MUSIC1"),
                  ]       
                  ]
        await message.reply("ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴇʀsᴏɴᴀʟ",
                            reply_markup=buttons)
        
    else:
        buttons = [[
            InlineKeyboardButton("⛩️𝐀ᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ Gʀᴏᴜᴘꨄ︎⛩️", url=f"https://t.me/{app.username}?startgroup=true")
        ]
        ]
        video = "https://graph.org/file/5fc8dd23ea909c8818e65.jpg"
        await message.reply_video(video, caption=f"""💌ʜᴇʟʟᴏ👻[{message.from_user.first_name}](tg://user?id={message.from_user.id}),
♦️ꭙ ɪ ᴀᴍ ʙwꜰ ᴄʜᴀᴛʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs 𓆪ꪾ🥀...

┏━━━━━━━━━━━━━━━━━━┓
┣🧸 𝐎𝐖𝐍𝐄𝐑   [👑𝐿2𝙍.🜲𝐊𝐈𝐍𝐆👑](https://t.me/L2R_KING0)
┣🍃 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 [💨𝐂𝐇𝐀𝐍𝐍𝐄𝐋💨](https://t.me/MUSICBOT_OWNER)
┣🍧 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 [💒𝐆𝐑𝐎𝐔𝐏💒](https://t.me/BWF_MUSIC1)
┣🦋 𝐒𝐎𝐔𝐑𝐂𝐄  [♕𝗔𝗦𝗛𝐈𝗦𝗛♕](https://t.me/II_ASHISH_GUPTA_IIl)
┗━━━━━━━━━━━━━━━━━━━┛
""", reply_markup=InlineKeyboardMarkup(buttons))

       
@bot.on_message(
    filters.command(["chatbot off", f"chatbot@{BOT_USERNAME} off"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vickdb = MongoClient(MONGO_URL)    
    vick = vickdb["VickDb"]["Vick"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "You are not admin"
            )
    is_vick = vick.find_one({"chat_id": message.chat.id})
    if not is_vick:
        vick.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Chatbot Disabled!")
    if is_vick:
        await message.reply_text(f"ChatBot Already Disabled")
    

@bot.on_message(
    filters.command(["chatbot on", f"chatbot@{BOT_USERNAME} on"] ,prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vickdb = MongoClient(MONGO_URL)    
    vick = vickdb["VickDb"]["Vick"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_vick = vick.find_one({"chat_id": message.chat.id})
    if not is_vick:           
        await message.reply_text(f"Chatbot Already Enabled")
    if is_vick:
        vick.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ChatBot Enabled!")
    

@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**ᴜsᴀɢᴇ:**\n/**chatbot [on/off]**\n**ᴄʜᴀᴛ-ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ(s) ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!**")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")

print(f"🎄 𝗖𝗛𝗔𝗧𝗕𝗢𝗧 𝗜𝗦 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗚𝗢 𝗔𝗡𝗗 𝗙𝗨𝗖𝗞🎄 ")      
bot.run()
#@ Mr.Daxx
