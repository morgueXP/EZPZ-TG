"""
Files Batch Uploader Plugin for userbot.
usage:- .upb 
Note:- set CHANNEL_ID and TEMP_DIR in Your ENV Vars First.
By:-@Zero_cool7870	

"""
import os 
import asyncio
from uniborg.util import admin_cmd
from telethon import events



@borg.on(events.NewMessage(pattern=r"\.upb", outgoing=True))
async def batch_upload(event):
	if event.fwd_from:
		return   
	if Config.CHANNEL_ID is None:
		await event.edit("Please Set Channel ID.")
		return
	if Config.TEMP_DIR is None:
		await event.edit("Please Set Temp Directory.")
		return
	in_channel = Config.CHANNEL_ID
	temp_dir = Config.TEMP_DIR	
	if os.path.exists(temp_dir):    
		os.chdir(temp_dir)
		files = os.listdir()
		files.sort()
		print(in_channel)
		await event.edit("Uploading Files on Telegram...")
		for file in files:
			required_file_name = temp_dir+"/"+file
			print(required_file_name)
			await borg.send_file(
					in_channel,
					required_file_name,
					force_document=True
				)
	else:
		await event.edit("Directory Not Found.")
		return		
	await event.edit("Successfull.")	
