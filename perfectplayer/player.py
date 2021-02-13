
import musicplayer as m
from time import sleep
import time
import os
import math
import CheckInput
#import lyrics


windoWidth=80


def printHelp():
	global windoWidth
	_ = os.system('cat readme.txt')
	clear()
	
	for i in range(windoWidth) :
		print("-",end='')

	for i in range(windoWidth) :
		print("-",end='')

	print("--Welcome to My music player--")
	print("\n\n 1.> run the player.py file by going to the file location and \n typing python player.py")
	print("\n 2.> now it should ask for song name you can simply enter song name \n and listen to it but \n  \n *Wait there is more")
	print("\n  || Use & to add multiple songs and \n  || -download to download the songs locally \n  || -video to see video of song \n")
	print("Once the player starts playing you can use jp 2 to jump to secong song and add song name to add new song to list and p to toggle",end='')
	print("pause/play and quit to exit and s to skip to next song and dl to look the downloaded list of songs\n \n")

def add(name,list):
	global playlist,output

	for i in range(windoWidth) :
		print('-',end='')

	print(playlist[1])
	songNumber=len(list)
	list.append(name[1:])
	#print('what is being seacrched is-',list[songNumber],'-')
	playlist[0].insert(songNumber, m.search(list[songNumber]))
	#print("song number is  - ",songnumb)
	playlist[1].insert(songNumber, m.title)
	#print(playlist)

	output.append('<'+str(len(output)+1)+".> "+playlist[1][songNumber])
	#print("output is ",output)
	print("Added -",playlist[1][songNumber])
	outputplaylist(output)
	return list


def clear(): 
	pass
	# for windows 
	if os.name == 'nt': 
		_ = os.system('clear')
		_ = os.system('cls') 
  
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = os.system('clear') 



def doControl(change,list,player):

	global songnumb

	if change[:3] == 'add' :
		list=add(change[3:],list)


	if change[:2] == 'dl':
		m.printDownloadedSongs()

	elif change[:2] == 'jp' :
		songnumb = int(change[3:])-2
		player.stop()
		return 's'

	elif change[:4] == 'goto':
		player.set_time(int(change[4:]))


	elif change[:1] == 'rm':
		print("here")
		playlist.remove(int(change[2:]))
		#player.set_time(int(change[4:]))


	elif 'p' in change :
		player.pause()

	elif 'r' in change :
		player.pause()

	elif 'q' in change :
		player.stop()
		return 'quit'

	elif 's' in change :
		player.stop()
		return 's'

	return 'f'

def outputplaylist(output):

	global windoWidth,palyer
	clear()
	songNumber=1;
	global songnumb
	#print('playing',player.is_playing())
	noOfLines=len(list)+8
	shift=7


	for o in range (noOfLines):

		if o == 0:
			continue

		if o == 1 or o == 2:
			for i in range(windoWidth) :
				print("-",end='')
			continue

		if o == 4:
			print('-- Now Playing -- ('+str(songnumb+1)+')',end='')
			for spc in range((windoWidth - (22+len(str(songnumb+1))))):
				print(' ',end='')
			print("||")
			continue

		if o == 6:
			for i in range(windoWidth) :
				print("-",end='')
			continue

		if o > 6 and o < noOfLines-1:
			
			print('  ',end='')
			if len(output[o-shift]) > windoWidth-3 :
				output[o-shift]=output[o-shift][:74]+".."
			print(output[o-shift],end='')
			for spc in range((windoWidth - len(output[o-shift])-4)):
				print(' ',end='')
			print("||")
			continue

		if o == noOfLines-1:
			for i in range(windoWidth) :
				print("-",end='')
			print()
			continue

		for spc in range((windoWidth -2)):
			print(' ',end='')
		print("||")

		songNumber=songNumber+1


	#durationof song currently played by player in sec

	duration=player.get_length()/1000

	print('Current song -',str(math.floor(duration/60))+":"+str(math.floor(duration%60))+' min')
	for i in range(windoWidth) :
		print("-",end='')
	print("\n   ")
	print("Enter add to add song dl to see downloads !help for more")


	#	lyrics.printLyrics(playlist[1][songnumb],duration)




print("\nEnter !help to learn how to use this player or enter the song name seprat by '&' \n")
list=[]
raw_songs=input('Enter songs - ')

if raw_songs[0:6] == '!help' :

	printHelp()
	list.insert(0,input("Enter songs-"))

if raw_songs == 'best' :

	list=(os.listdir(os.path.abspath("downloads/")))

else:
	if '&' in raw_songs :
		list=raw_songs.split('&')
		for i in range(len(list)) :
			list[i]=list[i].strip()
	else :
		list.insert(0,raw_songs.strip())

# Creates a list that contans your songs seprated by '&'

print(list)
player=''
#this is the vlc player 
playlist=[''],['']
#this is the playlist its first(zeroth) arry contains the url of songs and second (first) arry contain titles 
output=[]
#this contans the tilt with their apropeate numbers


for i in range(windoWidth) :
	print('-',end='')

for i in range(windoWidth) :
	print('-',end='')


#search songs here 
for songnumb in range(len(list)) :

	playlist[0].insert(songnumb,m.search(list[songnumb]))
	#print("song number is  - ",songnumb)
	playlist[1].insert(songnumb,m.title)
	#print(playlist)

songnumb=0
#getting output ready
for songnumb in range(len(playlist[1])-1):
	output.insert(songnumb,"<"+str(songnumb+1)+".> "+playlist[1][songnumb])



# playing songs here

songnumb=0
#this the number of song played from zero and is globaly used
while True :		

	startTime=time.time()
	#print(startTime)
	if len(playlist[1]) < songnumb:
		songnumb=songnumb-1

	if playlist[0][songnumb] == []:
		songnumb=songnumb-1
	player=m.player(playlist[0][songnumb])
	#else :
	
	print("Use add songname to add song")
	clear()
	#screen is cleared here
	outputplaylist(output)

	#sleep for vlc plyer to wake

	sleep(4)
	duration=player.get_length()/1000

	while time.time()-startTime < duration :
	
		
		#print('time is -',(time.time()-startTime),' duration is -',duration)
		



		readedVal=CheckInput.Read()
		
		if readedVal == 'pause':
			player.pause()
			time.sleep(0.5)

		if CheckInput.Read() == "read":
		
			change=input("change -")

			#refresh after every input
			clear()
			outputplaylist(output)

			a=doControl(change,list,player)
			if 's' in a :
				break
				print('done')
			if 'f' in a:
				continue
			if 'quit' in a:
				print("hope you had fun")
				quit()
			sleep(1)

	songnumb=songnumb+1

	print("song over")