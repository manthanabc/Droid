# Droido
currelty droido is an music player that searches music on youtube and plays on your pc without leaving the terminal with all sorts of cool features
## installing -
#### first install all dependecies
`pip install lyricsgenius`
`pip install dotenv      `
`pip install vlc`
`pip install pafy`
`pip install keyboard`
`pip install google`
`pip install bs4`
`pip install urllib.request`

#### setting up the .env file

- Get the youtube api key from [goole dev console][api]
and create a youtube api key and on first line on your .env file past it (past the key in place on 'your api key')

   `YOUTUBE_API_KEY='your api key'`
   

- for second key head over to lyrics gen site [optional] 
get the api key from [lyrics gen][u]
 `LYRICSGENIUS_API_KEY='your api key'`

and thats it now you can use all functions droido has to offer

## using the music player
from the perfectplayer directory run the following command to run the player
`python player.py`
then enter your music and enjoy
#### before playing
- you can use `&` to add multiple music
- use `-download` flag to download before playing
- use `-nolocal` flag to research and play
- use `-video` flag to play video with song

#### after playing

- press `p` to pause/ play
- use `a` to get the change menu
- use `add 'song name'` to add to que
- use `dl` to get list of downloaded songs
- use `s` to skip
- use `jp n` to jump to nth song(eg jp 2)
- use `q` to exit
[1]: https://console.developers.google.com
[api]: https://console.developers.google.com/ "api"
[u]: https://genius.com/developers
