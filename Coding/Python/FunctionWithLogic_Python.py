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