'''
from bs4 import BeautifulSoup
import urllib.request


def SearchVid(search):
    responce = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)

    soup = BeautifulSoup(responce)    
    divs = soup.find_all("div", { "class" : "yt-lockup-content"})


    for i in divs:
        href= i.find('a', href=True)
        print(href.text,  "\nhttps://www.youtube.com"+href['href'], '\n')
        with open(SearchString.replace("%20", "_")+'.txt', 'a') as writer:
            writer.write("https://www.youtube.com"+href['href']+'\n')

print("What are you looking for?")
SearchString = input()
SearchVid(SearchString.replace(" ", "%20"))
'''
'''
import urllib.request
from bs4 import BeautifulSoup

textToSearch = 'python tutorials'
query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
        print('https://www.youtube.com' + vid['href'])

'''