import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.google.com/search?q=python+beautifulsoup').read()#'https://pythonprogramming.net/parsememcparseface/'


soup = bs.BeautifulSoup(source,'lxml')


# title of the page


print(soup.title.text)

for url in soup.find_all('a'):
    print(url.get('href'))

'''
# get attributes:

# get values:
##print(soup.title.string)

# beginning navigation:
##print(soup.title.parent.name)

# getting specific values:
print(soup.p)
'''

'''
print(soup.find_all('p'))

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

for url in soup.find_all('a'):
    print(url.get('href'))
'''
#print(soup.get_text())
