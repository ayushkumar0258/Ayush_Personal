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