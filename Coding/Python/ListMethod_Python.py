############################ ? List method ########################
########################### ? append method for appending item into the last of the list ########
my_new_list=[2,5,4,6,67,'ayush','data',45.7]
my_new_list.append(56) #### it will append 56 in the last of the list
print("list values after appending are following. : ", my_new_list)
####################### ? pop method for removing last item from the list #################
my_new_list.pop()
print("list values after appending are following. : ", my_new_list)
my_new_list.pop()
print("list values after appending are following. : ", my_new_list)
my_new_list.pop()
print("list values after appending are following. : ", my_new_list)
my_new_list.pop(3)
print("list values after appending are following. : ", my_new_list)
my_new_list.pop(-2)
print("list values after appending are following. : ", my_new_list)
########################  ? sorting of the list ##############
#alp_list=['akash','Gupta','Hi','Good','r','t','e',1,55,67,43]
#alp_list.sort() # will throwing error because we are sorting mixed data type elements.
#print("above list after shorting is following.  ", alp_list)
alp_list=['akash','gupta','hi','good','r','t','e']
alp_list.sort() # this will short in alphabatical order. 
print("above list after shorting is following.  ", alp_list)
num_list=[3,5.6,7,2,3,9,12,2,1]
num_list.sort() ##### this will short the number in order here 5.6 will come after 3 as per order.
print("Number sorting list in python", num_list)
boolean_list = [True,False,1,4,3,3.5,2,8.9,45] ### we can't use string attribute in this because this list having true and false boolean that is like 1,2 only, so for shorting list should be of same data type, Here true and false considers as an integer type only.
same_time_assiged_list=boolean_list.sort()
print("Number sorting list in python", boolean_list)
shorted_boolean_list=boolean_list
print("shorted list assigned same time we use sort method:  ",same_time_assiged_list) # None will print because list assign to same_time_assigned_list same time we use .sort method as per the list sort method we are not assigning any thing. so result is None.
print("shorted list assigned after short the list :  ",shorted_boolean_list)

######################### ? List Reverse method #####################
Data_list=[3,56,1,2,45,34,2,3,8,9,76]
print("reverse list after applying reverse method on it ",Data_list.reverse()) ### will print none because if we are printing same time we are using reverse method then  it will throw the none becasue list.reverse() will throw none.
### but we print after applying reverse method then it will print the list in reverse order.
print("The list after reverse is following : ", Data_list) #this is printing list in reverse order because we apply .reverse on this list above the line here we are printing that list only.

########################### ? Nested list ##########
nested_list=[2,3,1,4,[3,5,6]]
print("We want to print the element from the nested list like i want to print 5 :::: ",nested_list[4][1])

### if list having set then how we can indexing the set element.
set_list=[2,4,1,5,{3,67,34}]
#print("We want to print the element from the nested set like i want to print 34 :::: ",set_list[4][2]) ## will throw error becasue set are not accepting ordering mean indexing....
print("We want to print the element from the nested set like i want to print set :::: ",set_list[4])
tuple_list=[2,4,1,5,(3,67,34)]
print("We want to print the element from the nested tuple like i want to print 34 :::: ",tuple_list[4][2])
########################### ? extend method : for extending the list by multiple items in one go ##############
exended_list=[45,34,23,45,67,89,2,3,1,4]
exended_list.extend([5,7,2,3])
print("list values after extending are following. : ", exended_list)

################################ ? insert - this method is used for inserting item in particular position ######
insert_list=[3,24,3,5,6,1,2]
insert_list.insert(3,77)
print("list values after extending are following. : ", insert_list)

############################### ? remove  - use for removing any value for the list that present in the list #####
new_list_Method=[45,67,23,45,34,21,11]
new_list_Method.remove(23)
print("new list after using remove method : ", new_list_Method)

############################ ? clear - for clearing the list ################
new_list_Method.clear()
print("new list after using remove method : ", new_list_Method)

######################### ? index - for finding the position of item in the list #########
new_list_Method1 =[34,6,'r','t',56,45,78,22,33,44]
print("Indexing for finding position of 78 in the list", new_list_Method1.index(78)) ## if we put value that not the part of list then throw the error.

################### ? copy - for making duplicate list ######### 
new_same_list=new_list_Method1.copy()
print("Copy of the list above is", new_same_list)

################### ? - count - this method tell the count of any particular number used in the list ###### 
print("the count of the number is ", new_same_list.count(22))