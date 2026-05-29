import urllib.request
data2=urllib.request.urlopen("http://data.pr4e.org/cover.jpg")
for lines in data2:
    print(lines.decode())
