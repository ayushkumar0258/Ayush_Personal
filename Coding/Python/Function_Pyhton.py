########## function 1 :  len function to get the length of a string########
my_data="my self ayush kumar and i am learning python"
print("Length of my data string are here : ",len(my_data))

########### function 2 : type function to get the type of variable ########
print("The type of my_data variable is : ", type(my_data))              

########### function 3 : str function to convert other data type into string ########
num1=45
num2=67.89
bool_var=True
print("The type of num1 is : ", type(num1))
print("The type of num2 is : ", type(num2))
print("The type of bool_var is : ", type(bool_var))
str_num1=str(num1)
str_num2=str(num2)
str_bool_var=str(bool_var)
print("The type of str_num1 is : ", type(str_num1))
print("The type of str_num2 is : ", type(str_num2))
print("The type of str_bool_var is : ", type(str_bool_var))     

######## function 4 : int function to convert other data type into integer ########
str_num3="123"
str_num4="45.67"
str_bool_var2="True"                
int_num3=int(str_num3)
int_num4=int(float(str_num4)) # We have to convert string to float first because
# directly converting string with decimal point to integer will cause a ValueError. By converting it to float first, we can then convert the float to an integer without any issues.
int_bool_var2=int(str_bool_var2 == "True") # This will convert the string "True" to the boolean value True, and then to the integer 1. If the string were "False", it would convert to the boolean value False, and then to the integer 0.
print("The type of int_num3 is : ", type(int_num3))
print("The type of int_num4 is : ", type(int_num4))
print("The type of int_bool_var2 is : ", type(int_bool_var2))               
######## function 5 : float function to convert other data type into float ######## 
str_num5="89.56"
str_num6="123"
str_bool_var3="False"
float_num5=float(str_num5)
float_num6=float(str_num6)
float_bool_var3=float(str_bool_var3 == "True") # This will convert the string
# "False" to the boolean value False, and then to the float 0.0. If the string were "True", it would convert to the boolean value True, and then to the float 1.0.
print("The type of float_num5 is : ", type(float_num5))
print("The type of float_num6 is : ", type(float_num6))
print("The type of float_bool_var3 is : ", type(float_bool_var3))           
######## function 6 : bool function to convert other data type into boolean ########
str_bool_var4="True"
str_bool_var5="False"       
str_num7="0"
str_num8="123"
bool_var4=bool(str_bool_var4 == "True") # This will convert the string
# "True" to the boolean value True. If the string were "False", it would convert to the boolean value False.
bool_var5=bool(str_bool_var5 == "True") # This will convert the string
# "False" to the boolean value False. If the string were "True", it would convert to the boolean value True.
bool_num7=bool(int(str_num7)) # This will convert the string "0" to the integer 0, and then to the boolean value False. In Python, the integer 0 is considered False, while any non-zero integer is considered True.            

bool_num8=bool(int(str_num8)) # This will convert the string "123" to the integer 123, and then to the boolean value True. In Python, any non-zero integer is considered True.
print("The type of bool_var4 is : ", type(bool_var4))
print("The type of bool_var5 is : ", type(bool_var5))
print("The type of bool_num7 is : ", type(bool_num7))
print("The type of bool_num8 is : ", type(bool_num8))




