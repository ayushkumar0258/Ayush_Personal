############# Try Except in Python #############
# The try-except block in Python is used to handle exceptions, which are errors that occur during the execution of a program. The try block contains the code that may raise an exception, while the except block contains the code that will be executed if an exception occurs. This allows you to gracefully handle errors and prevent your program from crashing. Here is the basic syntax of a try-except block:
# ```python
# try:
#     # Code that may raise an exception
# except ExceptionType:
#     # Code to handle the exception
# ```
# Here are some examples of how to use try-except blocks in Python:
# Example 1: Handling a ZeroDivisionError
try:
    result = 10 / 0  # This will raise a ZeroDivisionError because you cannot divide by zero.
except ZeroDivisionError:
    print("You cannot divide by zero!")  # This will print a message to the user indicating that they cannot divide by zero.
# Example 2: Handling a ValueError
try:
    number = int(input("Enter a number: "))  # This will raise a ValueError if the user enters something that cannot be converted to an integer.
except ValueError:
    print("Invalid input! Please enter a valid number.")  # This will print a message to the user indicating that they entered an invalid input.
# Example 3: Handling multiple exceptions
try:        
    result = 10 / 0  # This will raise a ZeroDivisionError.
    number = int(input("Enter a number: "))  # This will raise a ValueError if the user enters something that cannot be converted to an integer.
except ZeroDivisionError:
    print("You cannot divide by zero!")  # This will handle the ZeroDivisionError.
except ValueError:
    print("Invalid input! Please enter a valid number.")  # This will handle the ValueError.
# Example 4: Using a generic exception handler
try:
    result = 10 / 0  # This will raise a ZeroDivisionError.
except Exception as e:
    print(f"An error occurred: {e}")  # This will catch any exception that occurs and print the error message.  