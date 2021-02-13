

print("waking droido .",end=' ')
import os
import random
import numpy as np
import pafy
print('.',end=' ')
import keyboard
from time import sleep
print('.',end=' ')
import signal
import vlc
print('.')
import json
import tkinter as tk
from tkinter import *
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



def file_in_local(fi):
  arr=[]
  for i in os.listdir(os.path.abspath("downloads/")):
      if i.find(fi)!=-1:
        arr.append(i)
  return arr


def geo_query(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'

    ).execute()

    return video_response

     ########################################################3##############
'''
import tkinter
window = tkinter.Tk()
window.title("GUI")
# creating a function with an arguments 'event'
def say_hi(event): # you can rename 'event' to anything you want
 
    tkinter.Label(window, text = "Hi").pack()
btn = tkinter.Button(window, text = "Click Me!")
btn.bind("<Button-1>", say_hi) # 'bind' takes 2 parameters 1st is 'event' 2nd is 'function'
btn.pack()
window.mainloop()
..'''
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#


def pause():
  p.pause()
def quit():
  p.stop()

  '''

def search(urinput):
    next=1
#    urinput=input("Droido - ")
    if '-' in urinput:
      word,choice=urinput.split('-')
    else :
      word=urinput
      choice=''
    #word = input("Droido")
    #choice=input()
'''
'''

def load():
  test = youtube_search(word)

  vid=test[1]
  print(len(vid))
  print(vid[0]['id']['videoId'])

  url = vid[0]['id']['videoId']#"https://www.youtube.com/watch?v=bMt47wvK6u0"  #"https://www.youtube.com/watch?v=Q0bnAmfGQC8"

  video = pafy.new(url)

  best = video.getbest()
  bestaudio=video.getbestaudio()
  v=False
  if 'video' in choice :
    playurl = best.url#best.url
    v=True
  else : 
    playurl = bestaudio.url
  lst.append(playurl)

  #playurl=lst[0]
  '''
def play(playurl):
  global lst
  p=vlc.MediaPlayer(playurl)

  p.play
  print(best.title)
  print("playing.")
  print("use p to toggle pause and q to quit")
  sleep(4)
  while True:#p.is_playing():

    change=input()
    if 'p' in change :
      pause()
    if 'r' in change :
      resume()
    if 'q' in change :
      quit()
      break
    if 'next' in change:
      playurl=video[next].url
      next=next+1
    sleep(1)
  lst.remove(playurl)
  print("done")

#done with methods noe dicerct code
####################################################################################################

#data storing here ;;;

x = np.linspace(0, 1, 201)
y = np.random.random(201)

#You can store them very easily by doing the following:

np.savetxt('AA_data.dat', [x, y])


observations = ['Real', 'Fake']
flowers = ['Iris setosa', 'Iris virginica', 'Iris versicolor']

with open('DA_data.dat', 'w') as f:
    for _ in range(20):
        observation = random.choice(observations)
        flower = random.choice(flowers)
        f.write('{} {}\n'.format(observation, flower))


####################################################################################################
urinput=''
def assign(r,a):
  global urinput
  print('tryn to play ')
  urinput=a
  r.destroy

r = tk.Tk() 
r.title('Music Player') 
able=Label(r, text='Name').grid(row=0) 
print(able)
playbt = tk.Button(r,text=able, width=25,command=assign(r,able)).grid(row=1,column=0)
stopbt = tk.Button(r, text='Stop',fg='blue', width=25, command=r.destroy).grid(row=1,column=1)
e1 = Entry(r) 
e2 = Entry(r) 
e2.grid(row=0, column=1) 
#e1.grid(row=1,column=1)
r.mainloop()


next=1
if not urinput:
  urinput=input("Droido - ")

if '-' in urinput:
  choices=urinput.split('-')
  word=choices[0]
  choice=choices[1]

else :
  word=urinput
  choice=''
#word = input("Droido")
#choice=input()


favrates=['7','']


lst=[]

if file_in_local(word):
  print("playing from local")
  nam=file_in_local(word) 
  print(nam)
  playurl='/downloads/'+nam[0]
else:
  print("no local instance")
  test = youtube_search(word)
  vid=test[1]
  print(len(vid))
  print(vid[0]['id']['videoId'])

  url = vid[0]['id']['videoId']#"https://www.youtube.com/watch?v=bMt47wvK6u0"  #"https://www.youtube.com/watch?v=Q0bnAmfGQC8"

  video = pafy.new(url)

  best = video.getbest()
  bestaudio=video.getbestaudio()

  v=False

  if 'video' in choice :
    v=True
    playurl = best.url#best.url
  else : 
    playurl = bestaudio.url

  print(best.title)


  if 'downl' in choice :
    if v:
      best.download(filepath='/downloads/'+bestaudio.title+'.'+bestaudio.extension)
    else :
      bestaudio.download(filepath='/downloads/'+bestaudio.title+'.'+bestaudio.extension)

p=vlc.MediaPlayer(playurl)

p.play()

print("playing.")
print("use p to toggle pause and q to quit")
sleep(4)
while True:#p.is_playing():

    change=input()
    if 'p' in change :
      pause()
    if 'q' in change :
      quit()
      break
    sleep(1)
print("done")