"""
Anime Batch Downloader Plugin for userbot. //set TEMP_DIR Env Var first.
usage:- get a link of Animefrenzy.net Anime page and note number of eps they have.
cmd:- .anime num_of_eps page_link
By:- @Zero_cool7870	  

"""
from telethon import events
import asyncio
from bs4 import BeautifulSoup as bs 
import requests
import os
chunk_size =  3242880

download_dir=Config.TEMP_DIR	
try:
	os.makedirs(download_dir)
except:
	pass	


async def get_file_name(link):
	new_link = link[26:]
	l = ""
	for c in new_link:
		if c =='?':
			break
		l = l + c	
	l = l.replace("/","_")
	return l

async def download_file(url,filename):
	response = requests.get(url, stream=True)
	handle = open(filename, "wb")
	for chunk in response.iter_content(chunk_size=chunk_size):
		if chunk:  # filter out keep-alive new chunks
			handle.write(chunk)
	handle.close()   

async def get_download_links(download_link):
	size = len(download_link)
	lenk = ""
	count = 0
	for i in range(0,size):
		if i == size - 1:
			break
		lenk = lenk + download_link[count]
		count = count + 1
	return lenk	

@borg.on(events.NewMessage(pattern=r"\.anime", outgoing=True))
async def anime_download(event):
	urls = []
	if event.fwd_from:
		return   
	if Config.TEMP_DIR is None:
		await event.edit("Please Set Required ENV Variables First.")
		return

	
	var = event.text
	number_of_eps = var[7:9]
	number_of_eps = int(number_of_eps)
	number_of_eps = number_of_eps + 1 
	download_link = var[10:]  
	download_link = download_link[30:]
	download_link = "https://animefrenzy.net/"+download_link
	download_link = await get_download_links(download_link)
	await event.edit("Getting Download links...")
	for i in range(1,int(number_of_eps)):
		link = download_link+"-episode-"+str(i)+"/"
		res = requests.get(link)
		source = bs(res.text,'lxml')
		for a in source.find_all('a',{'class':'an'}):
			urls.append(a['href'])	
		
	counter = 0
	for url in urls:
		if "download.php?" in url:
			urls.pop(counter)	
		counter = counter + 1 

	counter = 0	
	for url in urls:
		if "#" in url:
			urls.pop(counter)	
		counter = counter + 1 
	await event.edit("Downloading Episodes...")
	for i in urls:
		filename = await get_file_name(i)
		print(filename)
		filename = download_dir+filename
		await download_file(i,filename)
	await event.edit("All Episodes Downloaded.")		
