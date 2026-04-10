my_list=[1,2,3,4,5,6,7,8,9,10]
my_list_mixed=[1,2,3.2,'ayush',True,[1,2,3],(4,5,6),{'name':'ayush','age':25}]
print("length of this list is : ",len(my_list_mixed)) # This will print the length of the list my_list_mixed, which is 7 because it contains 7 elements: an integer (1), a float (2.3), a string ('ayush'), a boolean (True), a list ([1,2,3]), a tuple ((4,5,6)), and a dictionary ({'name':'ayush','age':25}).
#print("length of this list is : ",my_list_mixed.len()) # ! This will cause an AttributeError because lists in Python do not have a len() method. To get the length of a list, we should use the built-in len() function instead, as shown in the previous line of code. For example:
################################### ? List indeexing and slicing ############################
print("First element of the above list id :", my_list[2]) # This will print the first element of the list my_list, which is 1. In Python, list indexing starts at 0, so my_list[0] refers to the first element, my_list[1] refers to the second element, and so on. Therefore, my_list[2] will refer to the third element of the list, which is 3.
print("Last element of the above list is : ", my_list[-1]) # This will print the last element of the list my_list, which is 10. In Python, negative indexing allows you to access elements from the end of the list. The index -1 refers to the last element, -2 refers to the second-to-last element, and so on. Therefore, my_list    [-1] will give you the last element of the list, which is 10.
print("Slicing of the list is : ", my_list[2:8:2]) # This will print a slice of the list my_list starting from index 2 up to index 8 (exclusive) with a step of 2. The output will be [3, 5, 7] because it includes the elements at indices 2, 4, and 6, which are 3, 5, and 7 respectively. The element at index 8 is not included in the output because the end index in slicing is exclusive. Therefore, the result is [3, 5, 7].
print("Slicing of the list is : ", my_list[1:10:3]) # This will print a slice of the list my_list starting from index 1 up to index 10 (exclusive) with a step of 3. The output will be [2, 5, 8] because it includes the elements at indices 1, 4, and 7, which are 2, 5, and 8 respectively. The element at index 10 is not included in the output because the end index in slicing is exclusive. Therefore, the result is [2, 5, 8].
print("Slicing of the list is : ", my_list[0:10:4]) # This will print a slice of the list my_list starting from index 0 up to index 10 (exclusive) with a step of 4. The output will be [1, 5, 9] because it includes the elements at indices 0, 4, and 8, which are 1, 5, and 9 respectively. The element at index 10 is not included in the output because the end index in slicing is exclusive. Therefore, the result is [1, 5, 9].         
print ("new slicing will be like :    ", my_list_mixed[1:7:1]) # This will print a slice of the list my_list_mixed starting from index 1 up to index 7 (exclusive) with a step of 1. The output will be [2, 3.2, 'ayush', True, [1, 2, 3], (4, 5, 6)] because it includes the elements at indices 1, 2, 3, 4, 5, and 6, which are 2, 3.2, 'ayush', True, [1, 2, 3], and (4, 5, 6) respectively. The element at index 7 is not included in the output because the end index in slicing is exclusive. Therefore, the result is [2, 3.2, 'ayush', True, [1, 2, 3], (4, 5, 6)].
print("Printing the my list on the bases of the indexing : ", my_list_mixed[5]) # This will print the element at index 5 of the list my_list_mixed, which is [1, 2, 3]. In Python, list indexing starts at 0, so my_list_mixed[0] refers to the first element, my_list_mixed[1] refers to the second element, and so on. Therefore, my_list_mixed[5] will refer to the sixth element of the list, which is [1, 2, 3].
print("the length of the list id: ")
print("Elements from list after 2 position : ",my_list[2:])
############################### ? List properties  ##############################
############################## ? Addition of two or more list #####################
another_list=['apple','Orange','Mango']
print("Combined all my)list and another_list together :  ",my_list+another_list) #this will combined both the list together by + sign
############################# ? Replacing element in the list ##################
my_list[3]='true'
print ("elements after replacing values are following : ", my_list)

