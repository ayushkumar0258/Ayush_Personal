import re
text='My 2 favorite numbers are 19 and 42'
y= re.findall('[0-9]+',text)
print(y)


print("Below expression for Greedy Matching               ::::")
x='F: Using the  characters'
y=re.findall('^F.+:',x)   ##### here nothing will print because as per expression it looking for starts with F and + mean at least one character before ends of :, But here no character between F and :
print(y)


print("Below expression for Greedy Matching               ::::")
x='F: Using the  characters'
y=re.findall('^F.*:',x) #### here F: will print becasue this expression is looking to start with F and * mean zero or more characters but here no character that mean it will still print because of *
print(y)

###################### below ? is used for stoping the greedy #################
print("Below expression for Greedy Matching               ::::")
x='F1: Using the :  characters : data'
y=re.findall('^F.+?:',x)   ##### here nothing will print because as per expression it looking for starts with F and + mean at least one character before ends of :, But here no character between F and :
print(y)


print("Below expression for Greedy Matching               ::::")
x='F: Using the :  characters : data'
y=re.findall('^F.*?:',x)   ##### here nothing will print because as per expression it looking for starts with F and + mean at least one character before ends of :, But here no character between F and :
print(y)

x='From ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('\S+@\S+',x)
print(y)

x='From ayushkumar.0258 @gmail.com sat jan 08 12:30:56 2026'
y=re.findall('\S*@\S+',x)
print(y)

################### Paranthess in regular expression ###############
x='From ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('^From (\S+@\S+)',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print(y)

x='F ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('^From (\S+@\S+)',x)  ############ ^From keyword for matching and inside ( ) afre the expression for extraction  
print(y)

x='From ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('^From (\S+@\S+)',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
list33=y[0].split('@')
print(list33[1])

x='From ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('@([^ ]*)',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print(y)

x='From ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('@([^ ]+)',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print(y)

x='From ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('@.+',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print(y)

x='From ayushkumar.0258@ gmail.com sat jan 08 12:30:56 2026'
y=re.findall('@.*',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print(y)

x='From ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('@(\S+)',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print(y)

x='From ayushkumar.0258@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('@(\S*)',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print(y)

x='From@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('^From.+@(\S+)',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print("New : ",y)

x='From@gmail.com sat jan 08 12:30:56 2026'
y=re.findall('^From.*@(\S+)',x)   ################ here () mean start and stop the regular expression finding here first will check starting with From the check expression defines in the paranthess
print("New : ",y)



import os
os.chdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/Coursera_Python")
file=open("mbox-short.txt")
new_list=[]
for lines in file:
    lines=lines.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',lines)
    if len(stuff) == 1:
        number=stuff[0]
        new_list.append(number)
    else:
        continue
max_num=max(new_list)
print("Bigger number is : ", max_num)


x='We have just pasi $10.00 to you'
y=re.findall('\$[0-9.]+',x)   ######## for searching and extraction $ we need to use backslace \ for this.
print(y)
