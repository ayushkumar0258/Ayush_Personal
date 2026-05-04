######## We have to use string in double quotes because some sentences having single quotes in it#######
#string_with_single_quotes = 'It's a nice day!'# ! This will cause a SyntaxError because the single quote in "It's" will be interpreted as the end of the string. To fix this, we can either use double quotes to define the string or escape the single quote using a backslash (\).
string_with_single_quotes_new = "It's a nice day!" # This will work correctly because we are using double quotes to define the string, allowing us to include the single quote without any issues.  
print("String with single quotes inside:", string_with_single_quotes_new)
print("New\tWord") ## \t is used to add a tab space between "New" and "Word"
print("New\nWord") ## \n is used to add a new line between "New" and "Word"
print("New\\Word") ## \\ is used to add a backslash between "New" and "Word"
print("She said, \"Hello!\"") ## \" is used to add double quotes inside a string defined by double quotes
print('She said, "Hello!"') ## This will work correctly because we are using single quotes to define the string, allowing us to include double quotes without any issues.       

string_properties ="Hello ji Good morning"
#string_properties[2]='P'
# ! This will cause a TypeError because strings in Python are immutable, which means we cannot change individual characters in a string after it has been created. To modify a string, we can create a new string by concatenating the desired changes. For example:
new_string=string_properties+'hey how are you'
print(new_string)
#new1_string=string_properties-'data'
#print(new1_string) # ! This will cause a TypeError because the subtraction operator (-) is not defined for strings in Python. To remove a substring from a string, we can use the replace() method or other string manipulation techniques. For example:
print(string_properties*10)
#print(string_properties/10) # ! This will cause a TypeError because the division operator (/) is not defined for strings in Python. To perform operations on strings, we can use string methods or other string manipulation techniques. For example:
print(5+4)
print('5'+'4') # This will concatenate the two strings '5' and '4' to produce '54', rather than performing arithmetic addition. To perform arithmetic addition, we need to convert the strings to integers first using the int() function. For example:
string_properties.isnumeric() # This will return False because the string "Hello" contains alphabetic characters and is not purely numeric.
string_properties.isalpha() # This will return True because the string "Hello" contains only alphabetic characters and no spaces or special characters.
string_properties.isalnum() # This will return True because the string "Hello" contains only alphanumeric characters (letters) and no spaces or special characters.
string_properties.isupper() # This will return False because the string "Hello" contains both uppercase and lowercase letters, and is not entirely in uppercase.
string_properties.islower() # This will return False because the string "Hello" contains both uppercase and lowercase letters, and is not entirely in lowercase.
string_properties.startswith("H") # This will return True because the string "Hello" starts with the character "H".
string_properties.endswith("o") # This will return True because the string "Hello" ends with the character "o".             
string_upper=string_properties.upper()
print("String in uppercase:", string_upper)
string_lower=string_properties.lower()
print("String in lowercase:", string_lower)
string_title=string_properties.title() #this used to make title text.
print("String in title case:", string_title)   
print(string_properties.split())
print(string_properties[3:25:2])     
print(string_properties.split('o')) # this will split the string at every occurrence of the character 'o' and return a list of the resulting substrings. The output will be ['Hell', ' ji G', 'od m', 'rning'] because the string "Hello ji Good morning" is split into four parts at each 'o'.
############# Question and answer#################
#Q. Can we change the value of a string in Python?
#A. No, strings in Python are immutable, which means we cannot change individual characters in a string after it has been created. To modify a string, we can create a new string by concatenating the desired changes. For example:
original_string = "Hello"
new_string = original_string + " World"
print(new_string) # This will output "Hello World" by concatenating the original string with the new string.                                    
#Q. What will be the output of the following code?
string_example = "Python"
print(string_example[1:4]) # This will output "yth" because it slices the string from index 1 to index 4 (exclusive), which includes the characters at indices 1, 2, and 3. The character at index 1 is "y", at index 2 is "t", and at index 3 is "h". The character at index 4 is "o", but since the end index is exclusive, it is not included in the output. Therefore, the result is "yth".     
#Q. How can we convert a string to uppercase in Python?
#A. We can convert a string to uppercase in Python using the upper() method. For example:
my_string = "Hello, World!"
uppercase_string = my_string.upper()
print(uppercase_string) # This will output "HELLO, WORLD!" by converting all characters in the original string to uppercase.
#Q. How can we check if a string starts with a specific substring in Python?
#A. We can check if a string starts with a specific substring in Python using the startswith() method. For example:
my_string = "Hello, World!"
print(my_string.startswith("Hello")) # This will return True because the string "Hello, World!" starts with the substring "Hello". If we check for a different substring, such as "Hi", it would return False because the string does not start with "Hi".      

############## ? - List of string methods in Python #################
#Case Conversion
#s = "hello world"
#s.upper()      # "HELLO WORLD"
#s.lower()      # "hello world"
#s.capitalize() # "Hello world"
#s.title()      # "Hello World"
#s.swapcase()   # "HELLO WORLD" -> "hello world"

#Searching & Checking
#s = "hello world"
#s.find("world")     # 6 (index)
#s.index("world")    # 6 (error if not found)
#s.count("l")        # 3
#s.startswith("he")  # True
#s.endswith("ld")    # True

#Boolean Checks
#s = "hello123"
#s.isalpha()   # False (has numbers)
#s.isdigit()   # False
#s.isalnum()   # True
#s.isspace()   # False
#s.islower()   # True
#s.isupper()   # False

#Modify Strings
#s = "  hello world  "
#s.strip()     # "hello world"
#s.lstrip()    # remove left spaces
#s.rstrip()    # remove right spaces
#s.replace("world", "Python")  # "hello Python"

#Split & Join
#s = "a,b,c"
#s.split(",")      # ['a', 'b', 'c']
#"-".join(["a","b","c"])  # "a-b-c"

#Alignment & Formatting
#s = "hello"
#s.center(10)   # '  hello   '
#s.ljust(10)    # 'hello     '
#s.rjust(10)    # '     hello'
#name = "Ayush"
#f"Hello {name}"   # formatted string

#Other Useful Methods
#s = "hello"
#len(s)        # 5
#s[0]          # 'h'
#s[::-1]       # reverse → "olleh"


##################