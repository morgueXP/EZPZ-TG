"""Globally Ban users from all the
feds where you are fedadmin in missrose_bot
Available Commands:
.fban @username REASON
.unfban @username """
from telethon import events
import asyncio
from uniborg.util import admin_cmd
from telethon.tl import functions, types

@borg.on(admin_cmd("fban ?(.*)"))
async def _(event):
    reason = event.pattern_match.group(1)
    if reason:
        await event.edit(f"Fbanned User Successfully")
    else:
        await event.edit(f"Fbanned that prick")
    await asyncio.sleep(5)
    await event.delete()
    try:
        await borg.send_message(  # pylint:disable=E0602
            Config.F_BAN_LOGGER_GROUP,  # pylint:disable=E0602
            f"/fban {reason}"
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602


@borg.on(admin_cmd("unfban ?(.*)"))
async def _(event):
    reason = event.pattern_match.group(1)
    await borg.send_message(
        Config.F_BAN_LOGGER_GROUP,
            "/unfban {reason}"
        )
    await event.edit("Unfbanned User Successfully")
