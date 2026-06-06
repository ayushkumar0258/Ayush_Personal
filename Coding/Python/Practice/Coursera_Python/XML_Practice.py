import urllib.request
import xml.etree.ElementTree as ET
url=urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_42.xml")
url_data=url.read()
#print(url_data)
XML_data=ET.fromstring(url_data)
#print(XML_data)
counts=list()
s=int(0)
for i in (XML_data.findall('.//count')):
    counts.append(i.text)
for j in counts:
    s=s+int(j)
print(s)

