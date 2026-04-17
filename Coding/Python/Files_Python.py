import os
with open("myfile.txt", "w") as myfile: ##### where this file will be created in the current directory
    myfile.write("This is my first file in python\n")
    myfile.write("This is the second line of the file\n")
    myfile.write("This is the third line of the file\n")    
# Reading the file
myfile = open("myfile.txt")
print(os.getcwd()) ##### to check the current working directory
print(myfile.read()) ##### to read the file
myfile.close() ##### to close the file after reading it 