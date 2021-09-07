from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhaba {message.from_user.first_name}!
Setting up
1) Botu ekleyip admin yapınız. 
2) Asistanı ekleyiniz asistan hesabı @flackwardev de
Commands
=>> Vidio Playing 🎧
- /stream : Reply to Video or File That You Want To stream In Vc.
- /stop  : Stop the stream
- /start :Start the bot
- /help  :To Help You
- /ly   : To Get lyrics Of Song
- /song : To Get Link From Youtube
- /quote: To Get Anime quote
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 Support Chat", url="https://t.me/burakizm"
                    )
                ]
            ]
        )
    )    
