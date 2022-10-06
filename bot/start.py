from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Merhaba!Ben telegram gruplarında görüntülü sohbette video yayını yapabilen bir botu. \n\n**Type /help komutlar için:-** __ \n1) Yazınız /info kurucu için`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Dev", url="https://t.me/burakizm")
                                    ]]
                            ))
   else:
      await m.reply("****")
