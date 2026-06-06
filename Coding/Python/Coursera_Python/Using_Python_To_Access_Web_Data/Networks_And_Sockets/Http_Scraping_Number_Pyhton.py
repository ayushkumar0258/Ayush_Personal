import urllib.request
import re
s=int()
data1=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2418984.html')
for line in data1:
    line=line.decode().strip()
    if (re.search('comments">([^<]*)',line)):
        d=re.findall('comments">([^<]*)',line)
        s=s+int(d[0])
print(s)
