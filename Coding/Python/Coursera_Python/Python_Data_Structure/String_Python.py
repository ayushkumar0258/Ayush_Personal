str1='ayush'
str2 =2
#str3=str1+str2
#print(str3) ### !- This will raise a TypeError because you cannot concatenate a string and an integer directly. To fix this, you can convert the integer to a string before concatenating:
str3 = str1 + str(str2)
print(str3)  # Output: "ayush2" 

#################### Taking input from user in python #####################
# In Python, you can take input from the user using the `input()` function. This function reads a line of text from the user and returns it as a string. You can also provide a prompt to the user by passing a string argument to the `input()` function. Here are some examples of how to take input from the user in Python:
# Example 1: Taking a simple input from the user
name = input("Enter your name: ")  # This will prompt the user to enter their name and store it in the variable `name`.
print("Hello, " + name )  # This will greet the user by printing a message that includes their name.
age=int(input("Age of the user: "))
#str4=name+age #### !- This will raise a TypeError because you cannot concatenate a string and an integer directly. To fix this, you can convert the integer to a string before concatenating:
str4 = name + str(age)
print(str4)  # Output: "Ayush25" (assuming the user entered "Ayush" as their name and "25" as their age)  

################ STring indexing and slicing in python ################
# In Python, strings are sequences of characters, and you can access individual characters or substrings using indexing and slicing. Indexing allows you to access a specific character in a string, while slicing allows you to access a range of characters. Here are some examples of string indexing and slicing in Python:
# Example 1: String indexing
my_string = "Hello, World!"
print(my_string[0])  # Output: "H" (the first character of the string)
print(my_string[7])  # Output: "W" (the eighth character of the string)
print(my_string[-1])  # Output: "!" (the last character of the string)
# Example 2: String slicing
my_string = "Hello, World!"
print(my_string[0:5])  # Output: "Hello" (the first five characters of the string)
print(my_string[7:12])  # Output: "World" (characters from index 7 to 11)
print(my_string[:5])  # Output: "Hello" (the first five characters of the string)
print(my_string[7:])  # Output: "World!" (characters from index 7 to the end of the string) 

############## Length of a string in python ##############
# In Python, you can find the length of a string using the built-in `len()` function. This function takes a string as an argument and returns the number of characters in the string,       
# including spaces and punctuation. Here are some examples of how to use the `len()` function to find the length of a string in Python:
# Example 1: Finding the length of a simple string
my_string = "Hello, World!"
length = len(my_string)  # This will return the length of the string, which is 13.
print(length)  # Output: 13
# Example 2: Finding the length of an empty string
empty_string = ""
length = len(empty_string)  # This will return the length of the empty string, which is 0.
print(length)  # Output: 0
# Example 3: Finding the length of a string with spaces
string_with_spaces = "   Hello, World!   "
length = len(string_with_spaces)  # This will return the length of the string, including the leading and trailing spaces, which is 19.
print(length)  # Output: 19     


######### STring concatenation in python ############
# In Python, you can concatenate strings using the `+` operator. This allows you to combine two or more strings into a single string. Here are some examples of string concatenation in Python:
# Example 1: Concatenating two strings
str1 = "Hello, "
str2 = "World!"
result = str1 + str2  # This will concatenate the two strings and store the result in the variable `result`.
print(result)  # Output: "Hello, World!"
# Example 2: Concatenating multiple strings
str1 = "Python "
str2 = "is "
str3 = "awesome!"
result = str1 + str2 + str3  # This will concatenate the three strings and store the result in the variable `result`.
print(result)  # Output: "Python is awesome!"
# Example 3: Concatenating strings with variables
name = "Ayush"
greeting = "Hello, " + name + "!"  # This will concatenate the string "Hello, ", the variable `name`, and the string "!" to create a greeting message.      

########## use of in operator with strings in python ############
# In Python, the `in` operator can be used to check if a substring exists within a string. It returns `True` if the substring is found in the string, and `False` otherwise. Here are some examples of how to use the `in` operator with strings in Python:
# Example 1: Checking if a substring exists in a string
my_string = "Hello, World!"
print("Hello" in my_string)  # Output: True (because "Hello" is a substring of "Hello, World!")
print("Python" in my_string)  # Output: False (because "Python" is not a substring of "Hello, World!")
# Example 2     : Checking if a character exists in a string
my_string = "Hello, World!"
print("H" in my_string)  # Output: True (because "H" is a character in "Hello, World!")
print("z" in my_string)  # Output: False (because "z" is not a character in "Hello, World!")
# Example 3: Checking if a substring exists in a string with case sensitivity
my_string = "Hello, World       !"
print("hello" in my_string)  # Output: False (because "hello" is not the same as "Hello" due to case sensitivity)
print("Hello" in my_string)  # Output: True (because "Hello" is a substring of "Hello, World!")     

######### STring comparison in python ############
# In Python, you can compare strings using the comparison operators such as `==`, `!=`, `<`, `>`, `<=`, and `>=`. These operators allow you to compare two strings and determine their relationship. Here are some examples of string comparison in Python:
# Example 1: Comparing two strings for equality
str1 = "Hello"
str2 = "Hello"
str3 = "World"
print(str1 == str2)  # Output: True (because str1 and str2 are the same string)
print(str1 == str3)  # Output: False (because str1 and str3 are different strings)
# Example 2: Comparing two strings for inequality
str1 = "Hello"
str2 = "World"
print(str1 != str2)  # Output: True (because str1 and str2 are different strings)
print(str1 != "Hello")  # Output: False (because str1 is the same as "Hello")
# Example 3: Comparing two strings for lexicographical order
str1 = "apple"
str2 = "banana"
print(str1 < str2)  # Output: True (because "apple" comes before "banana" in lexicographical order)
print(str1 > str2)  # Output: False (because "apple" does not come after "banana" in lexicographical order)
# Example 4: Comparing two strings with case sensitivity
str1 = "Hello"
str2 = "hello"
print(str1 == str2)  # Output: False (because "Hello" and "hello" are different due to case sensitivity)
print(str1.lower() == str2.lower())  # Output: True (because both strings are converted to lowercase before comparison)     

########### STring Libraries in python ############
# Python provides a rich set of libraries for working with strings. These libraries offer various functions and methods that can help you manipulate and analyze strings in different ways. Some of the commonly used string libraries  
# in Python include:
# 1. `str` library: This is the built-in string library in Python that provides various methods for string manipulation, such as `upper()`, `lower()`, `strip()`, `replace()`, and many more.
# 2. `re` library: This library provides functions for working with regular expressions, which are powerful tools for pattern matching and string manipulation.
# 3. `string` library: This library provides constants and functions for working with strings, such as `ascii_letters`, `digits`, `punctuation`, and more.
# 4. `textwrap` library: This library provides functions for formatting and wrapping text, which can be useful for displaying long strings in a more readable format.
# 5. `difflib` library: This library provides functions for comparing strings and finding differences between them, which can be useful for tasks such as spell checking and text comparison.
# These libraries can be imported and used in your Python code to perform various string operations and manipulations, making it easier to work with strings in your programs.      

##e.g., you can use the `str` library to manipulate strings as follows:
my_string = "   Hello, World!   "
print(my_string.upper())  # Output: "   HELLO, WORLD!   " (converts the string to uppercase)
print(my_string.lower())  # Output: "   hello, world!   " (converts the string to lowercase)
print(my_string.strip())  # Output: "Hello, World!" (removes leading and trailing whitespace)
print(my_string.replace("World", "Python"))  # Output: "   Hello, Python!   " (replaces "World" with "Python")  


############### to check dir for string library in python ##############
import string
print(dir(string))  # This will print a list of all the attributes and methods available in the `string` library, which you can use to manipulate and work with strings in Python.      


########## find method in string library in python ############
# The `find()` method in the `str` library is used to search for a substring within a string and returns the index of the first occurrence of the substring. If the substring is not found, it returns -1. The syntax for the `find()` method is as follows:
#```python
# string.find(substring, start, end)
#```
# Here, `substring` is the string you want to search for, `start` is the index from which to start the search (optional), and `end` is the index at which to end the search (optional). If `start` and `end` are not provided, the search will be performed on the entire string. Here are some examples of how to use the `find        ()` method in Python:
my_string = "Hello, World!"
print(my_string.find("World"))  # Output: 7 (the index of the first occurrence of "World" in the string)
print(my_string.find("Python"))  # Output: -1 (because "Python" is not found in the string)
print(my_string.find("o", 5))  # Output: 8 (the index of the first occurrence of "o" starting from index 5)
print(my_string.find("o", 5, 10))  # Output: -1 (because "o" is not found between index 5 and 10)

############# lstrip and rstrip method in string library in python ############
# The `lstrip()` and `rstrip()` methods in the `str` library are used to remove leading and trailing whitespace from a string, respectively. The `lstrip()` method removes whitespace from the left side of the string, while the `rstrip()` method removes whitespace from the right side of the string. The syntax for these methods is as follows:
#```python      
# string.lstrip()
# string.rstrip()
#```
# Here are some examples of how to use the `lstrip()` and `rstrip()` methods in Python:
my_string = "   Hello, World!   "
print(my_string.lstrip())  # Output: "Hello, World!   " (removes leading whitespace)
print(my_string.rstrip())  # Output: "   Hello, World!" (removes trailing whitespace)
print(my_string.strip())  # Output: "Hello, World!" (removes both leading and trailing whitespace)

########### STring prifix and suffix in python ############
# In Python, you can check if a string starts with a specific prefix or ends with a specific suffix using the `startswith()` and `endswith()` methods, respectively. The `startswith()` method checks if a string starts with a specified prefix and returns `True` if it does, and `False` otherwise. The `endswith()` method checks if a string ends with a specified suffix and returns `True` if it does, and `False` otherwise. The syntax for these methods is as follows:
#```python
# string.startswith(prefix)
# string.endswith(suffix)
#```
# Here are some examples of how to use the `startswith()` and `endswith()` methods in Python:
my_string = "Hello, World!"
print(my_string.startswith("Hello"))  # Output: True (because the string starts with "Hello")
print(my_string.startswith("World"))  # Output: False (because the string does not start with "World")
print(my_string.endswith("!"))  # Output: True (because the string ends with "!")
print(my_string.endswith("World"))  # Output: False (because the string does not end with "World")              

import os
print(os.getcwd())