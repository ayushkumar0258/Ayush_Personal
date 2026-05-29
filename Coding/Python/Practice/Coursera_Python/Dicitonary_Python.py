stuff = dict()
print(stuff['candy'])


dict={'a':45,'b':56,'c':99}
print('a' in dict)
print('z' in dict)


list1=[]
dict1={}
for i in range (6):
    list1.append(input("Enter the name : "))
for name in list1:
    if name not in dict1:
        dict1[name]=1
    else:
        dict1[name]=dict1[name]+1
print(dict1)
for k in dict1:
    print(k, dict1[k])
print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

for a,b in dict1.items():
    print (f"dict keys are {a} and values are {b}")

#print(dict1["ayush"])
try:
    print(dict1["ayush1"])
except:
    print("Not present")
print(dict1.get("ayush1"))

