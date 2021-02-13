
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from dotenv import load_dotenv

import vlc
import pafy
import os

load_dotenv()
DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"




def youtube_search(q, max_results=1,order="relevance", token=None, location=None, location_radius=None):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet",
    maxResults=max_results,
    location=location,
    locationRadius=location_radius

  ).execute()

  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result)
  try: 
      nexttok = search_response["nextPageToken"]
      return(nexttok, videos)
  except Exception as e:
      nexttok = "last_page"
      return(nexttok, videos)



def file_in_local(fi):

	if not os.path.exists("downloads/"):
		os.mkdir('downloads')
	#checks if downloads directory exists if nocreate one
	outarr={}
	out=[]
	words=fi.split()
	match=[]

	for wrd in words:
		for i in os.listdir(os.path.abspath("downloads/")):
			if i.lower().find(wrd.lower())!=-1 :
				if i in outarr:
					outarr[i]=outarr[i]+1
				else :
					outarr[i]=1

	songs=[]
	for song in outarr:
		print(song,outarr[song])
		songs.append([song,outarr[song]])

	for i in range(len(songs)-1):
		for j in range(1,len(songs)):
			if songs[j][1] > songs[j-1][1]:
				songs[j][1],songs[j-1][1]=songs[j-1][1],songs[j][1]


	for i in range(len(songs)):
		out.append(songs[i][0])

	print(songs)
	return out



def printDownloadedSongs():
	for i in os.listdir(os.path.abspath("downloads/")):
		print(i[:-5])
	print()

#this is the title of song curretly searched for
title=''

def player(url):

	p=vlc.MediaPlayer(url)
	p.play()

	return p


def download(song):
	
		song.download(filepath='/downloads/'+song.title+'.'+song.extension)


def search(inpu=''):

	global title

	videos=[]

	if '-' in inpu:
		a=inpu.split('-')
		word=a[0]
		choice=''
		for i in range(len(a)):
			choice=choice + a[i]
		#=urinput.split('-')
	else :
		word=inpu
		choice=''

	#if not 'nolocal' in choice :

	if file_in_local(word) and not 'nolocal' in choice:
			print("playing from local")
			nam=file_in_local(word) 
			#print(nam)
			splayurl='/downloads/'+nam[0]
			title=nam[0][:-4]
			#print('sent nam ehich is  ',nam)
			if not 'nolocal'in choice:
				return splayurl

	if not 'nolocal' in choice :
		print("no local instance")

	try:
		test = youtube_search(word)
	except HttpError as h:
		#print(h)
		if 'quota' in str(h):
			print("\n\nYoutube limit over we will try to remove thislimit in future versions\n")
			print("you can still hear this songs-")
			printDownloadedSongs()
			inp=input("enter choise- ")
			return search(inp)


	videos=test[1]
	#print(len(videos))
	#print(videos[0]['id']['videoId'])     # LINK OF VIDEO 

	# url = videos[0]['id']['videoId']#"https://www.youtube.com/watch?v=bMt47wvK6u0"  #"https://www.youtube.com/watch?v=Q0bnAmfGQC8"

	# if no video is found
	if not videos:
		print("no song found")
		return False


	#selec the first video

	video=videos[0]

	#print(video[0]['id']['videoId']) #uncomment to see the song url

	url = videos[0]['id']['videoId']
	# "https://www.youtube.com/watch?v=bMt47wvK6u0"
	#pafy is used to get the actual video in desired format and quality

	pafy_video = pafy.new(url)

	# getting the best vieo or audio from youtube for selected video

	best = pafy_video.getbest()
	bestaudio=pafy_video.getbestaudio()
	retur = ''
	#print("length is ; ",length)

	if 'v' in choice and not "audio" in choice:
		playurl = best.url#best.url
		title=best.title
		if 'dow' in choice:
			download(best)
		retur=best
	else :
		playurl = bestaudio.url
		title=bestaudio.title
		if 'dow' in choice:
			download(bestaudio)
		retur=bestaudio
	return playurl