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
    reason = event.pattern_match.group(1)
    await borg.send_message(
        Config.F_BAN_LOGGER_GROUP,
            "/fban {reason}"
        )
    await event.edit("Fbanned User Successfully")


@borg.on(admin_cmd("unfban ?(.*)"))
async def _(event):
    reason = event.pattern_match.group(1)
    await borg.send_message(
        Config.F_BAN_LOGGER_GROUP,
            "/unfban {reason}"
        )
    await event.edit("Unfbanned User Successfully")
