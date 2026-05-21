mylist=[]
for i in 'ayush':
    mylist.append(i)
print(mylist)


print("Below output after using the list comprehension in pyhton:  ")
my_new_list=[i for i in 'Kumar']
print(my_new_list)

print ("Below are the square of the number using the list comprehension : ")
square=[i*i for i in range(10)]
print("The square of the numbers are : ", square)

print("Even numbers using the list comprehension : ")
even=[i for i in range (100) if i%2==0]
print(even)


celcius_temp=[10,20,30,50,64.3]
feranite_temp=[((9/5)*i+32) for i in celcius_temp]
print("Temperature in feranite is : ", feranite_temp)

############### Temperature code #################

def tmp (t):
    f_t= ((9/5)*t+32)
    print("Temperature in feranite is following : ", f_t)
    choice=int(input("Do you wana to check for other temperature : if yes press  1 or 2 if No : "))
    if(choice==1):
        t_new=float(input("Please enter the temperature: "))
        tmp(t_new)
    else:
        print("Thanks for using : ")


tmp1=float(input("Please mention the temprature the celcius :  "))
tmp(tmp1)

############### Data are the following #############
odd_even=['EVEN' if (i%2==0) else 'ODD'  for i in range (100)]
print(odd_even)

odd_even=[i if (i%2==0) else 'ODD'  for i in range (20)]
print(odd_even)

#############  Nested For Loop ############
myList=[]
for i in range (3):
    for j in range (5):
        myList.append(i*j)
print(myList)


################ Nested for loop by using list comprehension ################
list5=[i*j for i in range (3) for j in range (4)]
print(list5)

list5=[i*j for i in range (3) for j in range (4)]
print(list5)
