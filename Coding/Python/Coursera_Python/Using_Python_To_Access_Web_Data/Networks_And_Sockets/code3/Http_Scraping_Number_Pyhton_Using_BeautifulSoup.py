import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_2418984.html'

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

total = 0

tags = soup.find_all('span')

for tag in tags:
    total = total + int(tag.text)

print(total)