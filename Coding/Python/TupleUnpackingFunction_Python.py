################### Tuple Unpacking in Python ###################
# Tuple unpacking is a powerful feature in Python that allows you to assign values from a tuple to multiple variables in a single line of code. This can make your code more concise and easier to read. The syntax for tuple unpacking is as follows:
# ```python
# variable1, variable2, variable3 = tuple
# ```
# Here, `variable1`, `variable2`, and `variable3` are the variables that will be assigned the values from the `tuple`. The number of variables on the left side of the assignment must match the number of elements in the tuple on the right side. If there are more variables than elements in the tuple, you will get a `ValueError`. If there are fewer variables than elements in the tuple, the remaining elements will be ignored.
# Here are some examples of tuple unpacking in Python:
# Example 1: Unpacking a tuple into variables
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
# Example 2: Unpacking a tuple with more variables than elements
my_tuple = (1, 2)
a, b, c = my_tuple  # This will raise a ValueError because there are more variables than elements in the tuple.
# Example 3: Unpacking a tuple with fewer variables than elements
my_tuple = (1, 2, 3)
a, b = my_tuple  # This will ignore the third element of the tuple and only assign the first two elements to the variables a and b.
print(a)  # Output: 1
print(b)  # Output: 2
# Example 4: Unpacking a tuple in a for loop
my_list = [(1, 2), (3, 4), (5, 6)]
for a, b in my_list:
    print(f"a: {a}, b: {b}")
# Output:
# a: 1, b: 2
# a: 3, b: 4
# a: 5, b: 6        