"""
Slaps a user
Note :- Change my_user_name string to your name before using this plugin kthxbye
Syntax: .slap
By :- Jaskaran ^_^ 
Telegram :- @Zero_cool7870

"""

import sys
from telethon import events, functions
from uniborg.util import admin_cmd
import random

my_user_name="Jaskaran ^_^"

ITEMS = (
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "CRT monitor",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "rubber chicken",
    "spiked bat",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
)

SLAP_MESSAGES=["'s Bot Pins you down and starts hitting on your Axs.","'s Bot hurls VoLTE Fix Right on your face.","'s Bot Flashes MIUI on Your Samsung Device, Now Rip.","'s Bot Throws RMM state at You","'s Bot grabs up a wine Bottle and hits Your Head Hard with it. :p"]
@borg.on(admin_cmd(pattern="slap ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    else:
        slap_msg = random.choice(SLAP_MESSAGES)
        slap_msg = my_user_name + slap_msg
        item = random.choice(ITEMS)
        #await event.edit("__"+slap_msg+"__")  
        await event.edit("__"+my_user_name + " 's bot starts slapping you with a "+item+"__")  
    
    