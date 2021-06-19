from Music.services.callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from Music.helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["join"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>**LOVISH is HERE TO PLAY MUSIC IN VC**</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "LOVISH"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"♪**LOVISH ASSISTANT IS HERE✨♪**")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>**LOVISH is HERE to paly MUSIC IN VC </b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Flood wait time out {user.first_name} try adding @LovishMusic_bot manually if cant.contact @PsychoBots_chat"
            "<b>Try adding @LovishMusic_bot manually</b>",
        )
        return
    await message.reply_text(
            "<b>@LovishMusic_bot is here ✨ </b>",
        )
    
@USER.on_message(filters.group & filters.command(["ubleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Contact support @PsychoBots_chat</b>."
            "<b>~byee byee</b>",
        )
        return
