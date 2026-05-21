########### Function in python ###########
def greet(name):     ## this is a function which takes a name as input and returns a greeting message.
    return "Hello, " + name + "!"     ## this will return the greeting message.
print(greet("Ayush"))     ## this will print the greeting message for Ayush.    

########### Function with default parameter value in python ###########
def greet(name="World"):     ## this is a function which takes a name as input and returns a greeting message. If no name is provided, it will use "World" as the default value.
    return "Hello, " + name + "!"     ## this will return the greeting message.
print(greet())     ## this will print the greeting message for World because we are not providing any name as input.
print(greet("Ayush"))     ## this will print the greeting message for Ayush because we are providing Ayush as input.           
#
# ############.  parameter **args in python ############
def print_args(*args):     ## this is a function which takes variable number of arguments and prints them.
    for arg in args:     ## this will iterate through the arguments and print them.
        print(arg)     ## this will print the argument.
print_args(1, 2, 3)     ## this will print the arguments 1, 2 and 3 because we are providing 1, 2 and 3 as input to the function.   
# ############.  parameter **kwargs in python ############
def print_kwargs(**kwargs):     ## this is a function which takes variable number of keyword arguments and prints them.
    for key, value in kwargs.items():     ## this will iterate through the keyword arguments and print them.
        print(f"{key}: {value}")     ## this will print the key and value of the keyword argument.
print_kwargs(name="Ayush", age=30)     ## this will print the keyword arguments name and age because we are providing name and age as input to the function. 
            