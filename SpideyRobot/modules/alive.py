from telethon import events, Button, custom
import re, os
from GreysonBot.events import register
from GreysonBot import telethn as tbot
from GreysonBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/1cd6d62ef6e8843e6b1cb.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**◐ I Aᴍ Aᴅᴠᴀɴᴄᴇᴅ Sᴘɪᴅᴇʏ Rᴏʙᴏᴛ !** \n\n"
  PIKACHU += "**◐ I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ**\n\n"
  PIKACHU += "**◐ Sᴘɪᴅᴇʏ! : 2.0 Lᴀᴛᴇsᴛ**\n\n"
  PIKACHU += "**◐ Mʏ Mᴀsᴛᴇʀ :** [DC Oᴡɴᴇʀ](t.me/DreamerNo1)\n\n"
  PIKACHU += "**◐ Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ : 1.23.0**\n\n"
  BUTTON = [[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ", "https://t.me/PigasusSupport"), Button.url("Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", "https://t.me/PigasusUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


__mod_name__ = "Alive⚜️"
