#Dictonaries use curly brackets and colons to signify the keys and their associated values.
######################### ? Dictonary - Syntax #########################
{'Key1': 'value1','key2':'value2'}
my_dict={'name':'Ayush','age':36,'phone':7895008172,'sex':'male'}
print("My dictonary are follwoing  : ",my_dict)
print("Printing the age from the dictonary. : ",my_dict['age']) #### Here we can see that dictonary can be ordered
dict_list_set_tuple_dict_data={'k1':23,'list':[2,1,34,2,3,56],'set':{45,67,45,3},'tuple':(23,45,23,45,67),'dict':{'k5':67,'k6':78}}
print("Want to print list 34 value : ",dict_list_set_tuple_dict_data['list'][2])
dict_list_set_tuple_dict_data['list'][2] ##### here we changes the value
print("Want to modify the 34 with 56 : ",dict_list_set_tuple_dict_data)
dict_list_set_tuple_dict_data['list'].remove(1) #### this will remove 1 from list given inside the dictonary.
print("Want to modify  : ",dict_list_set_tuple_dict_data)

