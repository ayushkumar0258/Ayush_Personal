######################## Printing list ##############
my_list=[('APPL',200),('GOOGL',300),('AMAZ',150)]
for i in my_list:
    print (i)

################ Printing item from the tuple unpacking #######

my_list=[('APPL',200),('GOOGL',300),('AMAZ',150)]
for item,price in my_list:
    print(f'hey value for {item} is {price}')


################### Using function employee of the year ##############
def employee_year(list1):
    Final_h=0
    Final_n=''
    for name,hours in list1:
        if(hours>Final_h):
            Final_h=hours
            Final_n=name
        else:
            pass
    return (Final_n,Final_h)

new_list=[('Ayush', 100),('Kumar',500),('ankit',900)]
item=employee_year(new_list)
print ("data of the employee of the year : ",item)
name1,hour1=employee_year(new_list)
print("Name of the employee is : ", name1)
print("Hours done by the employee is : ", hour1)
