# For @UniBorg
# (c) Shrimadhav U K
"""Auto Profile Updation Commands `.autoname .autobio`"""

import asyncio
import time
from telethon.tl import functions
from telethon.errors import FloodWaitError
from uniborg.util import admin_cmd


DEL_TIME_OUT = 70


@borg.on(admin_cmd(pattern="enautobio"))  # pylint:disable=E0602
async def _(event):
    await event.reply("Turned on Auto-Bio")
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | @SkuzzyWorld Don't mess with me | ⌚️ {HM}"
        logger.info(bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Bio"
            # )
        await asyncio.sleep(DEL_TIME_OUT)

        
@borg.on(admin_cmd(pattern="disautobio"))  # pylint:disable=E0602
async def _(event):
    await event.reply("Turned off Auto-Bio")
    if event.fwd_from:
        return
    while True:
        bio = f"@SkuzzyWorld Don't mess with me"
        logger.info(bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
            
            
@borg.on(admin_cmd(pattern="enautoname"))  # pylint:disable=E0602
async def _(event):
    await event.reply("Turned on Auto-Name")
    if event.fwd_from:
        return
    while True:
        DM = time.strftime("%d.%m.%y")
        HM = time.strftime("%H:%M")
        name = f"⌚{HM} | IN Skuzzy IN | 📅{DM}"
        logger.info(name)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Name"
            # )
        await asyncio.sleep(DEL_TIME_OUT)


@borg.on(admin_cmd(pattern="edisautoname"))  # pylint:disable=E0602
async def _(event):
    await event.reply("Turned on Auto-Name")
    if event.fwd_from:
        return
    while True:
        name = f"IN Skuzzy IN"
        logger.info(name)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
