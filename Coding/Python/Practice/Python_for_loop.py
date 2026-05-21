for _ in "Hello Ji":
    print("Cool!")
for _ in "Hello Ji":
    print(_)
list1= [(1,2,3),(4,5,6),(7,8,9)]
for i in list1:
    print(i)
for (a,b,c) in list1:
    print (a,b)
    print (c)
############### Dictonary example ########
d = {'k1':'hi','k2':'Good','k3':'morning'}
for i in d:
    print (d[i])
    
d = {'k1':100,'k2':200,'k3':300}
for i in d:
    print (d[i])
########## For printing full item mean with keys and values (we have to use the .items() #############
d = {'k1':100,'k2':200,'k3':300}
for i in d.items():
    print (i)
########## For printing only values of the key  mean with keys and values (we have to use the .values() #############
d = {'k1':100,'k2':200,'k3':300}
for i in d.values():
    print (i)

#################### for loop with range boundries ###########
for i in range (11,100):
    if(i % 9 == 0):
        print("Table of 9 is : " , i )

count=0
for i in 'ayush':
    print("the index are {} and values are following {}".format(count,i))
    count = count+1

for i in enumerate ('ayush'):
    print(i)

for ind,val in enumerate ('kumar'):
    print("The value at index {} is {}".format(ind,val))

for ind,val in enumerate ('kumar'):
    print(ind)
    #print('\n')
    print(val)

list1=[3,4,5,6]
list2=['a','b','c','d','e']
for i in zip (list1,list2):    ##### this zip used for combing the 2 list in which list1 will be index and another list2 will the value and here values will assign till minimum number of count. Here if you see list1 having 4 items and list2 having 5 items so that indexing will assign for first 4 items only.
    print(i)
list1=[3,4,5,6]
list2=['d','e']
for i in zip (list1,list2):    ##### this zip used for combing the 2 list in which list1 will be index and another list2 will the value and here values will assign till minimum number of count. Here if you see list1 having 4 items and list2 having 5 items so that indexing will assign for first 4 items only.
    print(i)
