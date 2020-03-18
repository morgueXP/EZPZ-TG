""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("alive"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "` This bot is more alive than you. ^.^ \n Me nub :/ \n\nTelethon version: 6.9.0\n Python: 3.7.3\nfork by:` @M0RGU3 \n`Give a man a program, frustrate him for a day,\n Teach a man to program,frustrate him for a lifetime. Go Die.!`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
