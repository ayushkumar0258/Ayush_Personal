def item_val(*data):
    for i in data:
        return data
item_val(2,3,4,5,6)


def new_multiple(**data):
    for key, values in data.items():
        print (f'{key} : {values}')

new_multiple(a=45,b=46)

data1= input("Please input the data : ")
choice = input ("Press 1 if you want to enter more inputs else 2  : ")
if (choice == '1'):
    data2=input("Please enter the data : ")
else : 
    data2=0
    print("Thanks for using:  ")
new_d=item_val(data1,data2)
print("data is following : ", new_d)

####################  Formatter during Function defination #############
def hello(h):
    print("My name is :  {}".format(h))
hello("ayush Kumar")


#################### With Default value in Function Parameter #########
def def_fun(h="Hello"):
    print(" HI i am here : {}".format(h))
def_fun()
def_fun("Ayush")


################### SUm of number function###########
def sumation(n1,n2):
    return (n1+n2)
sumation(34,45)
