############################### String Formating Method ######################
my_string = "Hello, World!"
print("Format method for the string", my_string.format('ayush')) # The format() method is used to format strings by replacing placeholders with specified values. In this case, since there are no placeholders in the string "Hello, World!", the format() method will simply return the original string without any changes. Therefore, the output will be "Hello, World!".
print("New data file {} {} {}".format('is','for','Python'))
print("New data file {2} {0} {1}".format('is','for','Python'))
name = "AYush Kumar"
print("My name is {}".format(name)) # This will replace the placeholder {} with the value of the variable name, which is "AYush Kumar". The output will be: My name is AYush Kumar
print(f"My name is {name}") # This is an f-string, which allows you to embed expressions inside string literals. The expression {name} will be evaluated and replaced with the value of the variable name, which is "AYush Kumar". The output will be: My name is AYush Kumar
print(f"My name is {name.upper()}") # This will convert the value of the variable name to uppercase using the upper() method and then embed it in the string. The output will be: My name is AYUSH KUMAR
print(f"My name is {name.lower()}") # This will convert the value of the variable name to lowercase using the lower() method and then embed it in the string. The output will be: My name is ayush kumar                                                   
roll=258  
subject="Mathematics"       
print(f"My name is {name} and my roll number is {roll} and i am studying subject {subject}")