################## We can retrive the html also using urllip ################
import urllib.request
import re
data1= urllib.request.urlopen("http://data.pr4e.org/page1.htm")
for lines in data1:
    print(lines.decode().strip())

print("****************************** Below output from page2 html calling from page1 html *************************************")
data1= urllib.request.urlopen("http://data.pr4e.org/page1.htm")
for lines1 in data1:
     #print(lines1.decode().strip())
     if(re.search('href="([^"]*)"',lines1.decode())):
        #print("YOU ARE HERE")
        data5=re.findall('href="([^"]*)"',lines1.decode())
        #print(data5[0])
        data6= urllib.request.urlopen(data5[0])
        for lines6 in data6:
            print(lines6.decode().strip())
    