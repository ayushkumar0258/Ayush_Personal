################# List Comprehensions in Python #################
# List comprehensions are a concise way to create lists in Python. They consist of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
# The syntax of a list comprehension is as follows:
# [expression for item in iterable if condition]
# Here, expression is the value to be added to the list, item is the variable that takes the value of the item in the iterable, and condition is an optional filter that determines whether the item should be included in the list or not.
# List comprehensions can be used to create new lists by applying an expression to each item in an iterable, optionally filtering items using a condition. They are often more concise and faster than using traditional for loops to create lists.
# Here are some examples of list comprehensions in Python:      
# Example 1: Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Example 2: Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens) # Output: [0, 2, 4, 6, 8]
# Example 3: Create a list of the first letter of each word in a list of words
words = ["hello", "world", "python", "programming"]
first_letters = [word[0] for word in words]
print(first_letters) # Output: ['h', 'w', 'p', 'p']
# Example 4: Create a list of tuples containing the number and its square for numbers from 0 to 9
num_square_tuples = [(x, x**2) for x in range(10)]
print(num_square_tuples) # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]       


#In list comprehension, if can be used in two different ways:
# At the end → for filtering
# At the beginning → for if-else value selection
even_or_odd = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(even_or_odd) # Output: ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']        
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers) # Output: [0, 2, 4, 6, 8]
    