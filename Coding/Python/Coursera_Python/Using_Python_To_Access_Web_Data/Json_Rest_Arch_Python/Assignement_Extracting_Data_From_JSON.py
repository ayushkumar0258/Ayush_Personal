import urllib.request
import json
url=input("Enter location: ")
print("Retrieving ",url)
data1=urllib.request.urlopen(url)
un=data1.read()
print("Retrieved ",len(un)," characters") 
data_final=json.loads(un)
count2=list()
s=int(0)
count2=data_final["comments"]
print("Count: ",len(count2))
for j in count2:
    s=s+int(j["count"])
print("Sum: ",s)