########### COllection of List in Python ############
# Lists are a built-in data structure in Python that can hold an ordered collection of items. They are mutable, which means that you can change the contents of a list after it has been created
# Lists are defined using square brackets [] and can contain items of different data types, including other lists. Here are some examples of how to create and use lists in Python:
# Example 1: Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
# Example 2: Creating a list with different data types
my_list = [1, "Hello", 3.14, [1, 2, 3]]
print(my_list)  # Output: [1, 'Hello', 3.14, [1, 2, 3]]
# Example 3: Accessing elements in a list
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
print(my_list[-1])  # Output: 5 (negative indexing starts from the end of the list)
# Example 4: Modifying elements in a list
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10  # This will change the first element of the list to 10
print(my_list)  # Output: [10, 2, 3, 4, 5]
# Example 5: Adding elements to a list
my_list = [1, 2, 3]
my_list.append(4)  # This will add the element 4 to the end of the list
print(my_list)  # Output: [1, 2, 3, 4]
my_list.insert(1, 10)  # This will insert the element 10 at index 1
print(my_list)  # Output: [1, 10, 2, 3, 4]
# Example 6: Removing elements from a list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  # This will remove the first occurrence of the element 3
print(my_list)  # Output: [1, 2, 4, 5]
my_list.pop(1)  # This will remove the element at index 1 (which is 2) and return it
print(my_list)  # Output: [1, 4, 5] 

######### List concatenation and repetition ##########
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Concatenation
list3 = list1 + list2
print(list3)  # Output: [1, 2, 3, 4, 5, 6]
# Repetition
list4 = list1 * 3
print(list4)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]     


########### List slicing ##########
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4] (slicing from index 1 to index 3, index 4 is not included)
print(my_list[:3])  # Output: [1, 2, 3] (slicing from the beginning to index 2)
print(my_list[2:])  # Output: [3, 4, 5] (slicing from index 2 to the end)
print(my_list[-3:])  # Output: [3, 4, 5] (slicing the last three elements of the list)  

########## List Methods ##########
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # This will add the element 6 to the end of the list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)  # This will insert the element 0 at index 0
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6]
my_list.remove(3)  # This will remove the first occurrence of the element 3
print(my_list)  # Output: [0, 1, 2, 4, 5, 6]
my_list.pop()  # This will remove the last element of the list and return it
print(my_list)  # Output: [0, 1, 2, 4, 5]
my_list.reverse()  # This will reverse the order of the elements in the list
print(my_list)  # Output: [5, 4, 2, 1, 0]
my_list.sort()  # This will sort the elements of the list in ascending order
print(my_list)  # Output: [0, 1, 2, 4, 5]   

############## in keyword in list ##############
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True (3 is in the list)
print(6 in my_list)  # Output: False (6 is not in the list)
print(3 not in my_list)  # Output: False (3 is in the list)
print(6 not in my_list)  # Output: True (6 is not in the list)

############# built-in functions with lists ##############
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5 (returns the number of elements in the list)
print(max(my_list))  # Output: 5 (returns the maximum element in the list)
print(min(my_list))  # Output: 1 (returns the minimum element in the list)
print(sum(my_list))  # Output: 15 (returns the sum of all elements in the list)

########### split of string make a list ############
my_string = "Hello, how are you?"
my_list = my_string.split()  # This will split the string into a list of words
print(my_list)  # Output: ['Hello,', 'how', 'are', 'you?'] (the split method splits the string by whitespace by default)

############ slipt on the bases of a specific character ############
my_string = "apple,banana,orange"
my_list = my_string.split(',')  # This will split the string into a list of fruits using the comma as the separator
print(my_list)  # Output: ['apple', 'banana', 'orange'] (the split method splits the string by the specified separator) 

