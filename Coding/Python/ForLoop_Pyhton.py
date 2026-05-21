import os # this will import the os module which is used to interact with the operating system.
import random # this will import the random module which is used to generate random numbers.S
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
#my_list=[1,2,3,4,5,6,7,8,9,10]
#list1=list(range(1,10))
#print(list1)    

################## enumerate function in for loop ############
my_list=[1,2,3,4,5,6,7,8,9,10]
for i in enumerate(my_list):     ## this will print the index and value         from list because we are using enumerate function to get the index and value from list.
    print(i)
for index, value in enumerate(my_list):     ## this will print the index and value from list because we are using enumerate function to get the index and value from list and we are using unpacking to get the index and value separately.
    print("the index is {} and value is {}".format(index, value))           
my_list=[7,8,9,10]
list1=['a','b','c','d','e']
for i in zip(my_list, list1):     ## this will print the value from list and list1 because we are using zip function to get the value from list and list1.
    print(i)
for i, j in zip(my_list, list1):     ## this will print the value from list and list1 because we are using zip function to get the value from list and list1 and we are using unpacking to get the value separately.
    print("the value from list is {} and value from list1 is {}".format(i, j))  


list3=[1,2,3,4,5]
list4=[6,7,8,9,10]
list5=[11,12,13,14,15]
for i in zip(list3, list4, list5):     ## this will print the value from list3, list4 and list5 because we are using zip function to get the value from list3, list4 and list5.
    print(i)

#print(list(zip(list3, list4)))     ## this will print the value from list3, list4 and list5 because we are using zip function to get the value from list3, list4 and list5 and we are using list function to convert the zip object to list.Since list3 and list4 have 5 elements and list5 has 5 elements, the zip function will only zip the first 5 elements of list3 and list4 and list5 and ignore the rest of the elements. So the output will be [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)] because we are zipping the first 5 elements of list3 and list4 and list5.

from os import listdir # this will import the listdir function from os module which is used to get the list of files and directories in a directory.
from os.path import isfile, join # this will import the isfile and join function from os.path module which is used to check if a path is a file and to join two paths respectively.
my_path = "C:/Users/Ayush/Desktop/Python" # this is the path of the directory which we want to get the list of files and directories.
#onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))] # this will get the list of files in the directory because we are using list comprehension to iterate through the list of files and directories and we are using isfile function to check if the path is a file and we are using join function to join the path of the directory and the name of the file to get the full path of the file and check if it is a file or not.
#print(onlyfiles) # this will print the list of files in the directory.      

random.shuffle(my_list) # this will shuffle the list because we are using shuffle function from random module to shuffle the list.
print(my_list) # this will print the shuffled list.