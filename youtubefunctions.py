import pafy

import keyboard

from time import sleep

import vlc

import json

       #####################################################################################


from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = "AIzaSyCMdhw8-rBtGwuK-HdDB4thUetjkNkn-hc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"




def youtube_search(q, max_results=10,order="relevance", token=None, location=None, location_radius=None):

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


def geo_query(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'

    ).execute()

    return video_response

     ########################################################3##############

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

word=''
playurl=''
next=1
lst=[]
choice=''
best=''
bestaudio=''
p=''
videoss=[]

def pause(p):
  p.pause()
def quit(p):
  p.stop()


def search(urinput=''):
  global word,choice,videoss
  if '-' in urinput:
    word,choice=urinput.split('-')
    #=urinput.split('-')
  else :
    word=urinput
    choice=''
    videoss = youtube_search(word)
    

def found():
  global videoss
  if(videoss):
    return True
  else:
    return False

def load():
  global word,lst,best,bestaudio,playurl,videoss
  if not videoss:
    return False
  vid=videoss[1]
  print(len(vid))
  print(vid[0]['id']['videoId'])

  url = vid[0]['id']['videoId']#"https://www.youtube.com/watch?v=bMt47wvK6u0"  #"https://www.youtube.com/watch?v=Q0bnAmfGQC8"

  video = pafy.new(url)

  best = video.getbest()
  bestaudio=video.getbestaudio()

  if 'v' in choice :
    playurl = best.url#best.url
  else : 
    playurl = bestaudio.url
  lst.append(playurl)
  #playurl=lst[0]

def play():
 global playurl,next,lst,word,p

 if(lst):
  p=vlc.MediaPlayer(lst[0])

  p.play()

  print(best.title)
  print("playing.")
  print("use p to toggle pause and q to quit")
 #    pass
  #   sleep(1)
  lst.remove(lst[0])
  print("done")
  #play()
  return p


def change(change):
	global p
	if 'pause' in change :
		pause(p)
	if 'q' in change :
		quit(p)
      	#break
		#return True
	if 'add' in change :
		word=change[3:]
		load()
		print("loaded at ",lst)
	if 'next' in change :
		#lst.remove(lst[0])
		play()


#search('once i was 7')

#load()

#play()

#while p.is_playing :
# 	change(input())
#lst.remove(lst[0])
#print("done")
#play()	