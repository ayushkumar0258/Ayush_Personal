##### set is the collection of unique items in python. it is unordered and unindexed data type in python. we can't access the item of set by using index because set is unindexed data type in python. set is mutable data type in python because we can change the value of set after creating it. set is defined by using curly braces {} in python. set is also used for removing duplicate values from the list in python. set is also used for performing mathematical operations like union, intersection.
a_set={1,2,3,4,2,3,78,90,56,45}
print("the type of a_set is : ",type(a_set))
print("the value of a_set is : ",a_set) ### this will print the unique value from the set because set is collection of unique items in python. so it will remove the duplicate values from the set and print only unique values.

##################### ? - add method - this method is used for adding new value in set ############
a_set.add(500)
print("the value of a_set after adding new value is : ",a_set)
