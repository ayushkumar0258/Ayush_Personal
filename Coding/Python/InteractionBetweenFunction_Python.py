################ Interaction between functions in python ################
# In Python, functions can call other functions, and this is a common practice in programming. This allows you to break down complex problems into smaller, more manageable pieces. When a function calls another function, the called function is executed, and once it finishes, the control returns to the calling function. This is known as function composition. Here are some examples of how functions can interact with each other in Python:  
# Example 1: A function that calls another function
def greet(name):
    return "Hello, " + name + "!"   
def welcome(name):
    greeting = greet(name)  # This will call the greet function and store the result in the greeting variable.
    return greeting + " Welcome to Python programming!"  # This will return the welcome message by concatenating the greeting and the welcome message.
print(welcome("Ayush"))  # This will call the welcome function with "Ayush" as the argument and print the welcome message for Ayush.  
# Example 2: A function that calls itself (recursive function)
def factorial(n):
    if n == 0:
        return 1  # Base case: the factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!
print(factorial(5))  # This will call the factorial function with 5 as the argument and print the factorial of 5, which is 120. 
    