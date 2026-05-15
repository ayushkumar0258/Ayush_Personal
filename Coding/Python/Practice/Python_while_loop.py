################ Syntax of while loop #################
#   while some_boolean_condition:
#   do something
#   else:
#   do something

i=0
while i<5:
    print("the sequence of the number is : ",i)
    i=i+1
else:
    print("all sequences has been completed ")
############# We have three main keyword (break,pass,continue) ###########
# Break : Breaks out of the current closet enclosing loop
# continue : Goes to the top of the closest enclosing loop
# pass : Does nothing at all

l=[1,2,3,4]
for i in l:
   pass
   print(i)
print("End of the loop")
print ("Below output for continue keyword")
l=[1,2,3,4]
for i in l:
   continue
   print(i)
print("End of the loop")


print ("Below output for break keyword")
l=[1,2,3,4]
for i in l:
   break
   print(i)
print("End of the loop")

print("Below are use of Break in while loop : ")
i=0
while i<5:
    print("the sequence of the number is : ",i)
    i=i+1
    break;
else:
    print("all sequences has been completed ")

print("Below are use of continue in while loop : ")
i=0
while i<5:
    print("the sequence of the number is : ",i)
    i=i+1
    continue;
else:
    print("all sequences has been completed ")

print("Below are use of pass in while loop : ")
i=0
while i<5:
    print("the sequence of the number is : ",i)
    pass;
    i=i+1
else:
    print("all sequences has been completed ")


print("Below are use of pass in while loop with if condition: ")
mystring='Sammy'
for i in mystring:
    if(i == 'a'):
       # print("the letter of string is following  : ",i)
        continue;
    else:
        print ("Other then a are following letters : ",i)
    
else:
    print("all sequences has been completed ")
