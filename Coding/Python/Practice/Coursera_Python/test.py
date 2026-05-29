import os
os.chdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/Coursera_Python")
name = input("Enter file:")
with open(name) as f:
    dicton={}
    for line in f:
        if line.startswith("From:"):
            list1=line.split()
            if list1[1] not in dicton:
                dicton[list1[1]]=1
            else:
                dicton[list1[1]]=dicton[list1[1]]+1
    largestnumber=0
    largestword=None
    for a,b in dicton.items():
        if b > largestnumber:
            largestnumber=b
            largestword=a
    print(largestword, largestnumber)
