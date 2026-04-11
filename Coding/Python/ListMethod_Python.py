############################ ? List method ########################
########################### append method for appending item into the last of the list ########
my_new_list=[2,5,4,6,67,'ayush','data',45.7]
my_new_list.append(56) #### it will append 56 in the last of the list
print("list values after appending are following. : ", my_new_list)
####################### pop method for removing last item from the list #################
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
