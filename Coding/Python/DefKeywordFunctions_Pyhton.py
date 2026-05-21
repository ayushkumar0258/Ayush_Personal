################## Def Keyword Functions in Python ##################
# In Python, the `def` keyword is used to define a function. A function is a reusable block of code that performs a specific task. Functions can take arguments, perform operations, and return values. The syntax for defining a function in Python is as follows:
# ```python
# def function_name(parameters):
#     # function body
#     return value
# ```
# Here, `function_name` is the name of the function, `parameters` are the inputs to the function (which can be optional), and the `function body` is the block of code that performs the task. The `return` statement is used to return a value from the function, but it is optional. If a function does not have a return statement, it will return `None` by default.
# Functions can be called by using their name followed by parentheses, and passing any required arguments. For example:
# ```python
# def greet(name):
#     return f"Hello, {name}!"
# print(greet("Alice"))  # Output: Hello, Alice!
# ```
# Functions can also have default parameter values, which are used if no argument is provided for that parameter when the function is called. For example:
# ```python
# def greet(name="World"):
#     return f"Hello, {name}!"
# print(greet())  # Output: Hello, World!
# print(greet("Alice"))  # Output: Hello, Alice!
# ```       
# Functions can also take variable-length arguments using `*args` for non-keyword arguments and `**kwargs` for keyword arguments. For example:
# ```python
# def print_args(*args):
#     for arg in args:
#         print(arg)
# print_args(1, 2, 3)  # Output: 1 2 3
# ```
# ```python
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_kwargs(name="Alice", age=30)  # Output: name: Alice age: 30
# ```

