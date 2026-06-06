import urllib.request
import xml.etree.ElementTree as ET
url=input("Enter location: ")
print("Retrieving ",url)
data1=urllib.request.urlopen(url)
un=data1.read()
print("Retrieved ",len(un)," characters")
data_final=ET.fromstring(un)
count2=list()
s=int(0)
count1=data_final.findall('.//count') ### how it is working? .// is used to find all the 'count' elements in the XML document, regardless of their position in the hierarchy. It searches through the entire document and returns a list of all 'count' elements it finds.
for i in count1:
    count2.append(i.text)
print("Count: ",len(count2))
for j in count2:
    s=s+int(j)
print("Sum: ",s)

