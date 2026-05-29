import os
print(os.getcwd())
file=input("Enter the file name you want to open:  ")
try:
    file2=open(file)
except:
    print("File name is not correct  ")
    quit()
for line in file2:
    l=line.find("from")  
    l2=line[l:]
    l3=l2.rstrip()
    print(l3)

