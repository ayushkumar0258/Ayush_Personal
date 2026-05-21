###################  Formatter during Function defination #############
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
print("Sum of those number are : ", sumation(34,45))


################### SUm of number function###########
def sumation(n1,n2):
    return (n1+n2)
print("Sum of those number are : ", sumation('34','45'))


################ Check even list ###############
def check_even_list(list1):
    for i in list1:
        if i%2==0:
            return True
        else:
            pass
    return False

print(check_even_list([23,53]))

#################### appending even number to one list ##############
even_list=[]
def check_even_list(list1):
    for i in list1: 
        if int(i)%2==0:
            even_list.append(i)
        else:
            pass
    print (even_list)
input_list=input("Please enter the list you want to validate : ").split()
check_even_list(input_list)
