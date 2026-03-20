# ################## ? - Data types use in python are below ############################################
# ################### ?- Interger - int  #############################
int =34
print("Interger Data type are ", type(int))

# #################### ?- Floating point - float ############################
float = 34.90
print ("Floating data type are ", type(float))
##################### ? String - str ############################
str="Ayush kumar"
print("String data type are ", type(str))
# ############################ ? -  List - list ###################################################
list1=[2,3,89,5,6]
#1. List is a collection which is ordered and changeable. Allows duplicate members.
list_duplicate=[2,3,89,5,6,2,3]
#2. List is defined by having values between square brackets [ ].
list_square_brackets=[2,3,89,5,6]
#3. List can have any number of items and they may be of different types (integer, float, string etc.). 
#list_different_types=[2,3.5,"Ayush",True,false]  ### ! NameError: name 'false' is not defined. Did you mean: 'False'?
list_different_types=[2,3.5,"Ayush",True,False] ##this list having different data types- integer,float,string and boolean
# 4. List items are indexed, the first item has index [0], the second item has index [1] etc.
print("List index[1] value is following" , list_different_types[1])
#5. List is mutable, which means we can change, add, and remove items in a list after it has been created.
list1[2]=55 # this will change the value of index 2 from 89 to 55
print("Modified list:", list1) 
list1.append(100) # this will add 100 at the end of the list
print("List after appending 100:", list1)
list1.insert(10,200) # this will insert 200 at index 10 but since index 10 is out of range, it will add 200 at the end of the list
print("List after inserting 200 at index 10:", list1)
# ! differencein append and insert is that append will always add the element at the end of the list while insert can add the element at any specified index in the list. If the specified index is out of range, it will add the element at the end of the list.
# ###################################### ?- Tuple - tuple #####################################################
#1. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
tuple_unchangeable=(1,2,3,4,5,7,7)
#2. Tuple is defined by having values between parentheses ( ).          
# 3. Tuple can have any number of items and they may be of different types (integer, float, string etc.).
tuple_different_types=(1,3.5,"Ayush",True,False) ##this tuple having different data types- integer,float,string and boolean
# 4. Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# 5. Tuple is unmutable, which means we cannot change, add, or remove
tuple_unmutable=(1,2,3,4,5)
#tuple_unmutable[3]=99 # ! This will cause a TypeError because tuples are immutable, which means we cannot change, add, or remove items in a tuple after it has been created.
# items in a tuple after it has been created. 
# 6. Tuple can be used as keys in a dictionary, while lists cannot because they are mutable.
# 7. Tuple can be used to store multiple items in a single variable, while lists are typically used to store collections of items that may need to be modified.
# 8. Tuple is generally faster than list when it comes to iteration and access because of its immutability, while lists are more flexible and can be modified after creation.
###################################### ?- Set - set ########################################################
#1. Set is a collection which is unordered and unindexed. No duplicate members.
set_unordered={1,2,9,6,3,4,5,7,7} # this will remove the duplicate value 7 and only one 7 will be present in the set will make order automatically because sets are unordered.
# Here unordered mean set the data in order.
print("Set after removing duplicate value 7:", set_unordered)
set_unordered2={7,1,3,5,4,2} # this will also remove the duplicate value 7 and only one 7 will be present in the set but the order of the elements may not be same as we have defined because sets are unordered.
print("Set after removing duplicate value 7 and unordered:", set_unordered2)
#2. Set is defined by having values between curly braces { }.
#3. Set can have any number of items and they may be of different types (integer, float, string etc.).
set_different_types={1,3.5,"Ayush",True,False,7,2,1} ##this set having different data types- integer,float,string and boolean
print("Set with different data types and duplicate value 1:", set_different_types) #remove true because true is 1 and false is 0 in python so it will remove true and only one 1 will be present in the set.
set_different_types2={3.5,"Ayush",True,False,7,2,6}
print("Set with different data types for set_different_types2:", set_different_types2) 
#4. Set items are unindexed, which means we cannot access items in a set by referring to an index, since sets are unordered.
set_data={1,2,3,4,5}
#set_data[2] # ! This will cause a TypeError because sets are unindexed.
#print("printing the set index values: ", set_data[3]) # ! This will cause a TypeError because sets are unindexed, which means we cannot access items in a set by referring to an index, since sets are unordered.
#5. Set is mutable, which means we can change, add, and remove items in a set after it has been created.
set_mutable={1,2,3,4,5}
set_mutable.add(6) # this will add 6 to the set
print("Set after adding 6:", set_mutable)
set_mutable.remove(2) # this will remove 2 from the set
print("Set after removing 2:", set_mutable)
#set_insert(3,67) # ! This will cause an AttributeError because sets do not have an insert method, since sets are unordered and do not support indexing.
################### ?- Dictionary - dict ########################################################
#1. Dictionary is a collection which is ordered and changeable. No duplicate members.
dict_ordered={"name":"Ayush", "age":25, "city":"Delhi", "name":"Ayush Kumar"} # this will remove the duplicate key "name" and only one "name" key will be present in the dictionary with the value "Ayush Kumar".
print("Dictionary after removing duplicate key 'name':", dict_ordered)
#2. Dictionary is defined by having values between curly braces { } and each item is a key-value pair separated by a colon :.
#3. Dictionary can have any number of items and they may be of different types (integer             , float, string etc.).
dict_different_types={"name":"Ayush", "age":25, "height":5.8, "is_student":True} ##this dictionary having different data types- string, integer                     , float and boolean
print("Dictionary with different data types:", dict_different_types)
#4. Dictionary items are indexed by keys, which can be of any immutable type (string, number, tuple etc.). The values can be of any type and can be accessed by referring to their keys.
print("Accessing value by key 'name':", dict_different_types["name"]) # this will access the value of key "name" which is "Ayush"
print("Accessing value by key 'age':", dict_different_types["age"]) # this will access the value of key "age" which is 25
print("Accessing value by key 'height':", dict_different_types["height"]) # this will access the value of key "height" which is 5.8
print("Accessing value by key 'is_student':", dict_different_types["is_student"]) # this will access the value of key "is_student" which is True
#5. Dictionary is mutable, which means we can change, add, and remove items in a dictionary after it has been created.
dict_mutable={"name":"Ayush", "age":25, "city":"Delhi"}
dict_mutable["age"]=26 # this will change the value of key "age" from 25 to 26
print("Dictionary after changing value of key 'age':", dict_mutable)
dict_mutable["height"]=5.8 # this will add a new key "height" with value 5.8 to the dictionary
print("Dictionary after adding key 'height':", dict_mutable)    
dict_mutable.pop("city") # this will remove the key "city" and its value from the dictionary
print("Dictionary after removing key 'city':", dict_mutable)
########## Below some Practicing ############
dict_pratcice={"Id":1000, "Name":"Ayush","Branch" : "Civil","Grade":"A"}
print("Practice Dictonary is following :", dict_pratcice)

######################## ? - Conclusion ########################################################################
# In conclusion, Python provides a variety of data types to store and manipulate different kinds of data. Each data type has its own characteristics and use cases, and understanding these data types is essential for effective programming in Python. Whether you are working with numbers, text, collections of items, or key-value pairs, Python has a data type that can help you manage and manipulate your data efficiently.        
# Please conclude the all the data types i python in table format for better understanding.

#Python Data Types Summary
#Data Type	    Example	                Mutable	    Ordered	    Allows Duplicates	      Description
#int	            10	                ❌ No	    ❌ No	    ❌ No	                Integer numbers
#float	            10.5                ❌ No	    ❌ No	    ❌ No                   	Decimal numbers
#complex	        2+3j	            ❌ No	    ❌ No	    ❌ No                   	Complex numbers
#str	            "Hello"	            ❌ No	    ✅ Yes	    ✅ Yes                  	Text/String
#list        	    [1, 2, 3]	        ✅ Yes      	✅ Yes	    ✅ Yes	                Ordered, changeable collection
#tuple	             (1, 2, 3)	        ❌ No	    ✅ Yes	    ✅ Yes	                Ordered, immutable collection
#set	            {1, 2, 3}	        ✅ Yes	    ❌ No	    ❌ No	                Unordered, unique elements
#dict	            {"a":1, "b":2}	    ✅ Yes	    ✅ Yes*	    ❌ (keys)	            Key-value pairs
#bool	            True / False	    ❌ No	    ❌ No	    ❌ No	                Logical values
#NoneType	         None	            ❌ No	    ❌ No	    ❌ No	                Represents no value
#📌 Important Notes

#✅ Mutable = Can be changed after creation (list, set, dict)

#❌ Immutable = Cannot be changed (int, float, str, tuple)

#📌 Ordered means data keeps insertion order

#dict is ordered from Python 3.7+

#📌 Set is fastest for:

#Checking duplicates

#Membership testing (in)

#🧠 Quick Memory Trick

#List → "Flexible" (change anytime)

#Tuple → "Fixed" (cannot change)

#Set → "Unique" (no duplicates)

#Dict → "Mapping" (key → value)

#If you want, I can also give you:
#✅ Interview questions on Python data types
#✅ Real-world use cases (very useful for backend/dev roles)
#✅ Small practice problems to master them quickly 🚀
######################## ? - String slicing in python ########################################################
# String slicing is a powerful feature in Python that allows you to extract a portion of a string by specifying a range of indices. The syntax for string slicing is as follows:
# ! string[start:end:step]
# - start: The index where the slice starts (inclusive). If omitted, it defaults to 0.
# - end: The index where the slice ends (exclusive). If omitted, it defaults to the length of the string.
# - step: The step size or stride between characters in the slice. If omitted, it defaults to 1.
# Here are some examples of string slicing in Python:
my_string = "Hello, World!"
print("Original string:", my_string)
# Slicing from index 0 to 5 (exclusive)
slice1 = my_string[0:5]
print("Slice from index 0 to 5:", slice1)
# Slicing from index 7 to the end of the string
slice2 = my_string[7:]
print("Slice from index 7 to the end:", slice2)
# Slicing the entire string with a step of 2
slice3 = my_string[::2]
print("Slice the entire string with a step of 2:", slice3)
# Slicing with negative indices (from the end of the string)
slice4 = my_string[-6:-1]
print("Slice with negative indices from -6 to -1:", slice4)
# Slicing with a negative step (reversing the string)
slice5 = my_string[::-1]
print("Slice with a negative step (reversed string):", slice5)
            