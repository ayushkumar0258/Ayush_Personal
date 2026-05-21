st1 = 'Print only the words that start with s in this sentence'
list1=st1.split()
for i in list1:
    if (i.startswith('s')):
        print(i)

#Use range() to print all the even numbers from 0 to 10.
for i in range(0,10):
    print (i)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
list2=[i for i in range (1,50) if (i%3==0)]
print(list2)

#Go through the string below and if the length of a word is even print "even!"
st1 = 'Print every word in this sentence that has an even number of letters'
list3=st1.split()
for i in list3:
    if (len(i) % 2 == 0):
        print("even! and having length : ", len(i))

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
print ("Below are the output for fizz and bizz problem :   ") 
for i in range (1,100):
    if(i%15==0):
        print("FizzBizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0):
        print("Fizz")
    else:
        print(i)

#Use List Comprehension to create a list of the first letters of every word in the string below:
st='Create a list of the first letters of every word in this string'
myList=st.split()
my_new=[i[0] for i in myList]
print(my_new)

