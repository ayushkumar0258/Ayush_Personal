import urllib.request
import xml.etree.ElementTree as ET
url= input("Enter the url : ")
xml_d=urllib.request.urlopen(url)
xml_data=xml_d.read()
data=ET.fromstring(xml_data)
list_data=list()
s=int(0)
for i in (data.findall('.//count')):
    list_data.append(i.text)

for j in list_data:
    s=s+int(j)
print('Sum : ',s)
