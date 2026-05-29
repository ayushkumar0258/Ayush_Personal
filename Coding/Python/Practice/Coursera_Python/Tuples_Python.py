list1=[1,2,3]
a, b, c=list1
print (a)
print (b)


d,e,f=23,45,56
print(d , e, f)

(g,h)=(77,88)
print(g,h)

dict1={'c':66,'b':56}
list1=[]
list2=[]
for a in dict1.items():

    list1.append(a)
print (list1)
for b in dict1.keys():
    list2.append(b)
print (list2)

sortedlist=sorted(dict1.items())
print(sortedlist)

sortedlist1=sorted(list2)
print(sortedlist1)
list3=[]
for a,b in dict1.items():
    list3.append((b,a))
print (list3)
print(sorted(list3))
print(sorted(list3,reverse=True))

t=tuple()
#print(dir(t))


file1 = input("Please enter the file name : ")
with open(file1) as file:
    dict34=dict()
    for lines in file:
        words=lines.split()
        for w in words:
            dict34[w]=dict34.get(w,0)+1
    #print(dict34)

    list55=[]
    list66=[]
    for a,b in dict34.items():
        if b>50:
            list55.append((b,a))
    for c,d in list55:
        list66.append((d,c))
    print(sorted(list66))
        
