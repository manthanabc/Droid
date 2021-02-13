from google import google
import bs4 as bs
import urllib.request


word = input("what you waqnt to seach - ")
num_page = 1
search_results = google.search(word, num_page)

for result in range(len(search_results)):
	print(result,'.>',search_results[result].description,"\n")

ch = int(input("\nchoice- "))




source = urllib.request.urlopen(search_results[ch].link).read()#'https://pythonprogramming.net/parsememcparseface/'

soup = bs.BeautifulSoup(source,'lxml')

print(soup.title.text)

for paragraph in soup.find_all('p'):
    print(str(paragraph.text))

'''

GoogleResult:
    self.name # The title of the link
    self.link # The external link
    self.google_link # The google link
    self.description # The description of the link
    self.thumb # The link to a thumbnail of the website (NOT implemented yet)
    self.cached # A link to the cached version of the page
    self.page # What page this result was on (When searching more than one page)
    self.index # What index on this page it was on
    self.number_of_results # The total number of results the query returned


from google import google, images
options = images.ImageOptions()
options.image_type = images.ImageType.CLIPART
options.larger_than = images.LargerThan.MP_4
options.color = "green"
results = google.search_images("banana", options)

'''