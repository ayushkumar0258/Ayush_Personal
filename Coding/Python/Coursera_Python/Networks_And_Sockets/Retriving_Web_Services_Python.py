################## urllib module is used to retrieve data from web services and it is a part of standard library in python ######################
import urllib.request
data1=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in data1:
    print(line.decode().strip())  ##### decode method is used to convert the byte format data to string format and strip method is used to remove the leading and trailing spaces from the string.


################# For printing same as a dictonary as per the words count #####################
import urllib.request
count=dict()
data2=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in data2:
    words=line.decode().split()
    for word in words:
        count[word]=count.get(word,0)+1
print(count)
