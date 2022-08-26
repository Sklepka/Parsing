from bs4 import BeautifulSoup
from urllib.parse import urlparse

html_file = open("skillbox.html", "r")
html_code = html_file.read()

soup = BeautifulSoup(html_code)


links = soup.findAll("a")
for link in links:
    print(link.attrs["href"])
