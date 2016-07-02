from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.cnn.com').read()
soup = BeautifulSoup(r, "lxml")
print type(soup)
