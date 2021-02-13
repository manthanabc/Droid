import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
import time
import os
from dotenv import load_dotenv
load_dotenv()

file = open("/Users/manthan/Desktop/lyrics_1.txt", "w")  # File to write lyrics to
genius = lg.Genius(os.getenv("LYRICSGENIUS_API_KEY"),  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)

#artists = ['Logic', 'Rihanna', 'Frank Sinatra']

'''
def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in arr
    c = 0  # Counter
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))  # Deliminator
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:  #  Broad catch which will give us the name of artist and song that threw the exception
            print(f"some exception at {name}: {c}")


get_lyrics(['alon'], 3)
'''
def printLyrics(raw_song,length):
	
	#raw_song=input()
	song = genius.search_song(raw_song)
	print("found song finding lyrics")
	s = song.lyrics
	print("found lyrics now printiong ")
	#length=163
	broken = s.split('\n')

	file.write(str(s))

	print(len(broken))

	for i in range(int(len(broken)/4)):
		number= i*4
		print(broken[i])
		print(broken[i+1])
		print(broken[i+2])
		print(broken[i+3])
		time.sleep(length/(len(broken)/4))
		_ = os.system("cls")