import webbrowser
import bs4
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup

name = input("Enter the name of 'TV SHOW/SERIES' you want to search : ")
print ("*** Your Downloading will start very soon ***")
link = "https://www.thepiratebay.org/search/"+name+"/0/99/0"
page = urlopen(Request(link, headers={'User-Agent': 'Mozilla'}))
page_html = page.read()
page1 = soup(page_html, "html.parser")	
a=page1.findAll("a", {"class": "detLink"})
a1=a[0]
a1["href"]
linknew = 'https://www.thepiratebay.org'+a1["href"]
page2 = urlopen(Request(linknew, headers={'User-Agent' : 'Mozilla'}))
page2_html = page2.read()
page3 = soup(page2_html , "html.parser")
page4 = page3.findAll("div", {"class" : "download"})
b = page4[0]
c = b.findAll("a", {"title":"Get this torrent"})
d = c[0]
e = d["href"]

webbrowser.open_new(e)
print ("Message : ***Thanks for using this***")
