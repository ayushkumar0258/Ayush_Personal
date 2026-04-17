# Tuple is similar to the list but it is immutable (Cannot be change after creating).
# tuplr used parenthsis for createing tuple.
tuple_syntax = (1,2,3,4,5,6)
t = (1,2,3,4,5,6,7)
mylist=[23,45,24,67,89,90]
print("the type of t is : ",type(t))
print("the type of mylist is : ",type(mylist))
################# ? Indexing and slicing in tuple is same as list ############
print("the value of 3rd index in tuple is : ",t[3])
print("the slicing of the tuple is : ",t[1:])
print("the slicing of the tuple is : ",t[1:6]) ###### this will print the value from index 1 to 5 because last index is exclusive in slicing.
print("the slicing of the tuple is : ",t[1:6:2]) #### this will print the value from index 1 to 5 with step of 2.
print("Printing the tuple values from last ", t[:6])
print("Printing the tuple values from last ", t[-2:])
print("Printing the tuple values from last ", t[:-2])
print("Printing the tuple values from last ", t[:-2:2]) #### this will print the value from index 0 to 4 with step of 2.    
###################### ? - count methid - this method is used for counting the number of times a value is present in tuple ############
print("the count number 2 in tupe list : ", t.count(2))

######################### ? - index method - this method is used for getting the index of first occurence of value in tuple ############
print("the index of value 4 in tuple is : ", t.index(4))
#################### ? - len method - this method is used for getting the length of tuple ############
print("the length of the tuple is : ", len(t))

################# ? - min and max method - this method is used for getting the minimum and maximum value from tuple ############
print("the max value in the tuple is : ", max(t))
print("the min value in the tuple is : ", min(t))

################ ? - copy method - this method is used for copying the tuple ############
#new_tuple= t.copy() #### ! this will throw error because tuple is immutable and it does not have copy method but we can copy the tuple by assigning the tuple to new variable.
new_tuple = t
print("the new tuple after copying is : ", new_tuple)

##################### ? Add new value in tuple ############
#t[3]=100 #### ! this will throw error because tuple is immutable and we can't change the value of tuple after creating it but we can add new value in tuple by concatenating two tuple.
t = t + (100,) #### this is the syntax for adding new value in tuple by concatenating two tuple here we are adding new value 100 in tuple t by concatenating it with another tuple (100,) here we are using comma after 100 because if we are not using comma then it will consider 100 as integer and not as tuple.
print("the new tuple after adding new value is : ", t)

####### Second method for adding new values in tuple ###########
list=list(new_tuple)
print("values present in list : ",list) 
list.append(200)
print("values present in list after adding new value : ",list)
new_tuple=tuple(list)
print("the new tuple after adding new value is : ", new_tuple)

########################### ? - tuple having inbulid 2 method - count and index method only because tuple is immutable and we can't change the value of tuple after creating it but we can add new value in tuple by concatenating two tuple. so we can't use any method for changing the value of tuple but we can use count and index method for counting the number of times a value is present in tuple and getting the index of first occurence of value in tuple. so these are the only two methods that we can use in tuple.
