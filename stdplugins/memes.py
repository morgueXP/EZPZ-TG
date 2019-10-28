# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
#
""" Userbot module for having some fun. """

import asyncio
import random
import re
import time

from cowpy import cow

from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register


@register(pattern=r".scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    """ Just a small command to fake chat actions for fun !! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@",
                                                             "!"):
        options = [
            'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
            'photo', 'document', 'cancel'
        ]
        input_str = event.pattern_match.group(1)
        args = input_str.split()
        if len(args) is 0:  # Let bot decide action and time
            scam_action = random.choice(options)
            scam_time = random.randint(30, 60)
        elif len(args) is 1:  # User decides time/action
            try:
                scam_action = str(args[0]).lower()
                scam_time = random.randint(30, 60)
            except ValueError:
                scam_action = random.choice(options)
                scam_time = int(args[0])
        elif len(args) is 2:  # User decides both action and time
            scam_action = str(args[0]).lower()
            scam_time = int(args[1])
        else:
            await event.edit("`Invalid Syntax !!`")
            return
        try:
            if (scam_time > 0):
                await event.delete()
                async with event.client.action(event.chat_id, scam_action):
                    await asyncio.sleep(scam_time)
        except BaseException:
            return



CMD_HELP.update({"memes": "Ask 🅱️ottom🅱️ext🅱️ot (@NotAMemeBot) for that."})
