########## String indexing #######
str1='banana'
for i in range(len(str1)):
    print(f"At index {i} :",str1[i])


########### Counting a from the string banana ###########
str2='banana'
count=0
for i in str2:
    if (i == 'a'):
        count=count+1
print(count)

############# String comparision Lower case is bigger then the upper cases that why below condition is true.  ##########
str1='bat'
str2='Bat'
if(str1>str2):
    print("True")

########################## String Library ################
str1="Data Here to CheCK"
str2="Module"

print("Lower the string :   ", str1.lower())
print("Upper the string :   ", str1.upper())
print("Replace the string : ", str1.replace("Data","New"))
print("Striping the string   :  ", str1.strip())

############ String method ###############
str4='Ayush'
print(dir(str4))
print(str4.islower())


############## find method ##########
str1="Hey my name ayush kumar and i  am working in TCS Israel "
print(str1.find('a',50))

text = "X-DSPAM-Confidence:    0.8475"
ind1=text.find('0')
print(text[ind1:])

############# Print Text ############
print("Hey My name is Ayush Kumar")