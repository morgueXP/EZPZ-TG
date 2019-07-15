from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd, humanbytes, progress, time_formatter

@borg.on(events.NewMessage(pattern=r"\.getc", outgoing=True))
async def get_media(event):
    if event.fwd_from:
        return
    dir= "./temp/"
    try:
        os.makedirs("./temp/")
    except:
    	pass
    channel_username= event.text
    limit = channel_username[6:9]
    print(limit)
    channel_username = channel_username[11: ]
    print(channel_username)
    await event.edit("Downloading  All Media From this Channel.")
    msgs = await borg.get_messages(channel_username, limit=int(limit))
    with open('log.txt','w') as f:
    	f.write(str(msgs))
    for msg in msgs:
       if msg.media is not None:
	        await borg.download_media(
                msg,dir)
             