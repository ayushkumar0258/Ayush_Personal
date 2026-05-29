########### tuple assignment in Python ############
# Tuple assignment is a powerful feature in Python that allows you to assign values to multiple variables in a single line of code. This is done using parentheses and commas to create a tuple on the left side of the assignment. The number of variables on the left side must match the number of values in the tuple on the right side. Here are some examples of tuple assignment in Python:
# Example 1: Basic tuple assignment
a, b, c = 1, 2, 3
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3       

# Example 2: Tuple assignment with different data types
name, age, city = "Ayush", 25, "New York"
print(name)  # Output: Ayush
print(age)  # Output: 25
print(city)  # Output: New York     

# Example 3: Tuple assignment with a list
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Example 4: Tuple assignment with a function that returns multiple values
def get_coordinates():
    return 10, 20   
x, y = get_coordinates()
print(x)  # Output: 10
print(y)  # Output: 20  

######## Tuples are Comparable ############
# In Python, tuples are comparable, which means that you can compare two tuples using comparison operators such as <, >, <=, >=, ==, and !=. The comparison is done element by element, starting from the first element of each tuple. If the first elements are equal, the comparison moves on to the second elements, and so on, until a difference is found or the end of the tuples is reached. Here are some examples of tuple comparison in Python:
# Example 1: Comparing two tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 < tuple2)  # Output: True (because 3 is less than 4)
print(tuple1 > tuple2)  # Output: False (because 3 is not greater than 4)
print(tuple1 == tuple2)  # Output: False (because the tuples are not equal)
print(tuple1 != tuple2)  # Output: True (because the tuples are not equal)
# Example 2: Comparing tuples with different lengths
tuple3 = (1, 2)
tuple4 = (1, 2, 3)
print(tuple3 < tuple4)  # Output: True (because the first two elements are equal, but tuple3 has fewer elements than tuple4)
print(tuple3 > tuple4)  # Output: False (because the first two elements are equal, but tuple3 has fewer elements than tuple4)
print(tuple3 == tuple4)  # Output: False (because the tuples are not equal)
print(tuple3 != tuple4)  # Output: True (because the tuples are not equal)  

######### sorting list of tuples based on the first element of the tuple ############
my_list = [(3, 'three'), (1, 'one'), (2, 'two')]
my_list.sort()  # This will sort the list of tuples based on the first element of each tuple
print(my_list)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]    

######### sorted method to sort list of tuples based on the second element of the tuple ############
my_list = [(3, 'three'), (1, 'one'), (2, 'two')]
sorted_list = sorted(my_list, key=lambda x: x[1])  # This will sort the list of tuples based on the second element of each tuple using a lambda function as the key argument
print(sorted_list)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]        