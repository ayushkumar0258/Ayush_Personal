####### For loop in python #######
for i  in  range(1, 11):     ## this will print the value from 1 to 10 because last index is exclusive in range function.
    print(i)            
for i in range(1, 11, 2):   ## this will print the value from 1 to 10 with step of 2 because we are using step of 2 in range function.
    print(i)
for i in range(10, 0, -1):  ## this will print the value from 10 to 1 because we are using step of -1 in range function.
    print(i)
for i in range(10, 0, -2):  ## this will print the value from 10 to 1 with step of -2 because we are using step of -2 in range function.
    print(i)            
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:              ## this will print the value from list because we are using for loop to iterate through the list.
    print(i)
for i in "Ayush":            ## this will print the value from string because we are using for loop to iterate through the string.
    print(i)    

list=[22,33,44,55,66,77]
for i in range(len(list)):        ## this will print the value from list because we are using for loop to iterate through the list and we are using range function to get the index of the list.
    print(list[i])         ## this will print the value from list because we are using index to get the value from list.
#######
my_list=[1,2,3,4,5,6,7,8,9,10]
list1=list(range(1,10))
print(list1)    

################## enumerate function in for loop ############
my_list=[1,2,3,4,5,6,7,8,9,10]
for i in enumerate(my_list):     ## this will print the index and value         from list because we are using enumerate function to get the index and value from list.
    print(i)
for index, value in enumerate(my_list):     ## this will print the index and value from list because we are using enumerate function to get the index and value from list and we are using unpacking to get the index and value separately.
    print("the index is {} and value is {}".format(index, value))           

        