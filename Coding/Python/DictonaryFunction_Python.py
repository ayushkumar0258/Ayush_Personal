#Dictonaries use curly brackets and colons to signify the keys and their associated values.
######################### ? Dictonary - Syntax #########################
dict_syntax={'Key1': 'value1','key2':'value2'}
my_dict={'name':'Ayush','age':36,'phone':7895008172,'sex':'male'}
print("My dictonary are follwoing  : ",my_dict)
print("Printing the age from the dictonary. : ",my_dict['age']) #### Here we can see that dictonary can be ordered
dict_list_set_tuple_dict_data={'k1':23,'list':[2,1,34,2,3,56],'set':{45,67,45,3},'tuple':(23,45,23,45,67),'dict':{'k5':67,'k6':78}}
print("Want to print list 34 value : ",dict_list_set_tuple_dict_data['list'][2])
dict_list_set_tuple_dict_data['list'][2] ##### here we changes the value
print("Want to modify the 34 with 56 : ",dict_list_set_tuple_dict_data)
dict_list_set_tuple_dict_data['list'].remove(1) #### this will remove 1 from list given inside the dictonary.
print("Want to modify  : ",dict_list_set_tuple_dict_data)

#dict_list_set_tuple_dict_data['set'][2] ### ! this will throw an error that set are not accepting indexing becasue set not follow ordered. and only set is in pythin that not follow ordered mean indexing.

################################ ? clear - this method used for clearing the dictonary ###########
print("Currently dict is looking like ", dict_syntax.clear()) ### ! this will return none becasue method is work like this only.
print("Currently dict is looking like ", dict_syntax) #### this will print the empty dictonary because .clear method clear full dictonary.

############################# ? copy - this method used for copying the dictory ###########
new_dict = dict_list_set_tuple_dict_data.copy()
print ("new dictonary after copy is  :  ", new_dict)

############################# ? pop -  this method used for removing any value based on key ############
#new_dict.pop() ###### this method we are using in list as well but difference is if we use pop() in list it remove last item from the list but in dictonary this is not acceptable.
print ("new dictonary after copy is  :  ", new_dict)
new_dict.pop('tuple')
print("dictonary after removing tuple key value from dictonary",new_dict)

########################### ? fromKey() - this will create a new dictonary with key mentioned ###########
keys=['k1','k2','k3']
dict_data=dict.fromkeys(keys,22) ##### this is the syntax for this method for making a new dictonary.
print("dictonary after removing tuple key value from dictonary",dict_data)

############### ? get() - this method for getting key values from dictonary ############ 
data1=new_dict.get('list')
print("dictonary after removing tuple key value from dictonary",data1)

################### ? items() - this method used for getting data with key in tuple format #########
items_dict=new_dict.items()
print("dictonary after removing tuple key value from dictonary :   ",items_dict)

################### ? keys() - this for getting all dictonary key ############## 
key1=new_dict.keys()
print("dictonary after removing tuple key value from dictonary",key1)

################ ? popitem() - this method is used for removing last key item from dictonary ############
new_dict.popitem()
print("dictonary after removing tuple key value from dictonary",new_dict)
