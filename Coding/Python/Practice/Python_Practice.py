dict={"id":"300","name":"Arushi","gender":"Male","mob":"7895008172"}
print("Printing the gender of the directory   :   ",dict["gender"])
dict["rollNo"]=1366577
print("newly added key value : ",dict)
dict.pop("name")
print("Directory after removing key name  : ", dict)
#########################################
tuple_data=(2,4,5,6,3,2,3,5,6,8)
print("current tuple date    :  ",tuple_data)
print("Value at index 3 are following : ",tuple_data[3])
tuple_newData=("ayush",67.78,True,"Hi",1,2,3)
print("Data of new tuple are follwoing : ",tuple_newData)
set_data={3,5,3,4,4,5,5,6,7,8,5,8,9,1,9}
print("Newly created set data are following : ",set_data)

set_data.remove(4)
print("Newly update value qith index 6 are following   : ", set_data)
set_data.add(2)
print("Set value after adding 2 : ", set_data)
set_data.add(0)
print("set value after adding 0 in set : ",set_data)
set_data.add(5)
print("Adding 5 into set, 5 value already exists : ",set_data)

print("module is :", 45%5)
print("dividing number :",57/7)
print("Exponational are following : ",9**5)
print("Floor division give us Quotient making round to below  : ",47//8 )
########################################
my_data=5
my_data=9
my_data="Ayush Kumar"
print("Till here value in my_data is : ",my_data)
my_data=True
my_data=67.89
print("Value are following : ",my_data)
my_data=["Hi","Ji","Kumar",78,45,True]
print("We can set any collection on it : ",my_data)
my_data=(4,3,5,4,6,7,23.90)
print("New data tuple assign to same data_type : ", my_data)
print("Data type till here should be tuple : ",type(my_data))
my_data={4,5,4,3,4,6,7,6,8,9,"Hi","Ji","Hi"}
print("new set assign to same date type :",my_data)
print("Currently data type are ", type(my_data))
################################## String slicing Practice ###########
name="Ayush Kumar0258"
slice1=name[:3]
print("The String slice1 is :  ",slice1)
slice2=name[2:8]
print("The string slice2 is : ",slice2)
slice3=name[::]
print("the string slice3 is : ", slice3)
slice4=name[2:9:3]
print("the string slice4 is : ",slice4)
slice5=name[-9:-3]
print("the string slice5 is : ",slice5)
slice6=name[::-2]
print("the string slice6 is : ", slice6)

num=234
print("the type of this data",type(num))
str_num=str(num)
print("New string data type of num", type(str_num))
str_string="My Name is AYush"
print("Indexing values of this string",str_string[0])
print("Indexing values of this string",str_string[0])
print("the type of this data",type(num))
str_num=str(num)
print("New string data type of num", type(str_num))
str_string="My Name is AYush"
print("Indexing values of this string",str_string[0])
print("Indexing values of this string",str_string[0])

str_string="My Name is AYush"
#float_string =float(str_string)
#print("Indexing values of this string",type(float_string))

sting_for_int="True"
#print("Data type for the this object",type(int(float(sting_for_int))))

#print("the type of this data",type(sting_for_int))
print("new sting to int data type",type(int((sting_for_int=="hey my love"))))
num2=45.87
int2=int(num2)
print(type(int2))
########### float type conversion ##########
num1=45
float1=float(num1)
print(type(float1))
str22="Ayush"
float3=float(str22=="Ayush")
print(type(float3))
print("Value for float3",float3)
print("String start with Hello", str22.startswith("A"))
str='JIJIJI'
print("First letter",str[1])
print("New file is having following data ".format())
print("New file {3} {2} {1} {0}".format('dictionary','letter','data','Hey'))
print("New file {} {} {} {}".format('dictionary','letter','data','Hey'))
print("New file {2} {2} {3} {2}".format('dictionary','letter','data','Hey'))
print("Hey ayush {0} you {1}".format('how', 'doing'))
print("Hey ayush {} you {} {} {} {}".format('how', 'doing','i','am','Good'))
