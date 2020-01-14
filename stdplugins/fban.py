"""Globally Ban users from all the
feds where you are fedadmin in missrose_bot
Available Commands:
.fban @username REASON
.unfban @username """
from telethon import events
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd("fban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            Config.F_BAN_LOGGER_GROUP,
            "/fban {}".format(reason)
        )
    await event.edit("Fbanned User Successfully")


@borg.on(admin_cmd("unfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            Config.F_BAN_LOGGER_GROUP,
            "/unfban {}".format(reason)
        )
    await event.edit("Unfbanned User Successfully")
