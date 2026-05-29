import os
os.chdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/Coursera_Python")
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dict555=dict()
for line in handle:
    if line.startswith("From "):
        list1=line.split()
        print(list1)
        words=list1[5]
        list2=words.split(':')
        if list2[0] not in dict555:
            dict555[list2[0]]=1
        else:
            dict555[list2[0]]=dict555[list2[0]]+1
for a, b in sorted(dict555.items()):
    print(a, b)