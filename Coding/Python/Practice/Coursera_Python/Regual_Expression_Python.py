import os
os.chdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/Coursera_Python")
file=open("mbox-short.txt")
for lines in file:
    lines = lines.rstrip()
    if lines.find("From:")>=0:   ############## find method return the index of string that we are looking for... here >=0 mean index at 0 or more then 0 mean it will success when and only when string will find the respective line. else -1
        print (lines)



############# using regular expression #############
print ("****************************** Below output from regular expression *************************************")
import re
file1=open("mbox-short.txt")
for line in file1:
    line=line.rstrip()
#    print(re.search('From:',line))
    if re.search('From:',line):
        print(line)

############## we can take the same result using the simple if condition###############
print ("****************************** Below output from simple if condition  *************************************")
file2=open("mbox-short.txt")
for line2 in  file2:
    line2=line2.rstrip()
    if "From:" in line2:
        print(line2)

############## we can take the same result using the startswith method ###############
print ("****************************** Below output from simple startswith method  *************************************")
file2=open("mbox-short.txt")
for line2 in  file2:
    line2=line2.rstrip()
    if line2.startswith('From:'):   ##### this expression will  return true is From keyword will present else will return False
        print(line2)

print ("****************************** Below output from regular (^From) expression *************************************")
file1=open("mbox-short.txt")
for line in file1:
    line=line.rstrip()
 #    print(re.search('From:',line))
    if re.search('^From:',line):  ####### The ^ symbol is used to indicate that the pattern should match only at the beginning of the line.
        print(line)

############### above both expression will give the same result because startswith () method is used to get the true result when the line start with the given string and in regular expression we are using ^ symbol to get the true result when the line start with the given string. ############

print ("****************************** Below output from regular (^X-C.*) expression *************************************")
file55=open("mbox-short.txt")
for line55 in file55:
    line55=line55.rstrip()
    if re.search('^X-C.*', line55):
        print (line55)

print ("****************************** Below output from regular (^X-\S+) expression *************************************")
file66=open("mbox-short.txt")
for line66 in file66:
    line66=line66.rstrip()
    if re.search('^X-Content-Type-Mess\S+:', line66):
        print (line66)
