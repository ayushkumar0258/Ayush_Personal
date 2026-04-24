import os
os.chdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice") ##### to change the current working directory to the given path
os.system("ls")
############################ ?  with open ("filename", "w") - this file will create at the current working directory . this will create file if not exsits with the same name and if file exists with same name then it will overwrite file with the new content. ##############
with open("myfile.txt", "w") as myfile: 
    myfile.write("This is my first file in python\n")
    myfile.write("This is the second line of the file\n")
    myfile.write("This is the third line of the file\n")    
# Reading the file
print(os.getcwd()) ##### to check the current working directory
myfile1 = open("myfile.txt")
print(myfile1.read()) ##### to read the file
myfile.close() ##### to close the file after reading it 
with open("myfile.txt", "w") as myfile: ##### here this "w" mode has been overwrite the file because with same name file was already exists.
    myfile.write("This is my first file in python\n")
    myfile.write("This is the second line of the file\n")
    myfile.write("This is the third line of the file56\n")    

############################# ? with open ("file name", "x") - this will create a new file in case file not exists with same name at working directory, in case file exists with same name it will give error that file already exists. if we want to overwrite the file then we can use "w" mode instead of "x" mode. ##############
#with open("myfile.txt",'x') as my_newFile: 
    ######## !- this will not overwrite the file if file exists with same name at working directory, it will give error that file already exists. if we want to overwrite the file then we can use "w" mode instead of "x" mode.
#with open("myfile_x2.txt",'x') as my_newFile: ##### this will create a new file in case file not exists with same name at working directory, in case file exists with same name it will give error that file already exists.
    #my_newFile.write("Hey this is new file")
    #my_newFile.write("Hey it is good to see you")
    #my_newFile.write("Hey Good to see you again")

######################### ? with open ("File Name", "r") - this will read the file if file exists with same name at working directory, in case file not exists with same name it will give error that file does not exist. ##############
with open ("myfile.txt", "r") as readfile:
    print(readfile.read())

################ ? with open ("File Name", "a") - this will append the content in the file if file exists with same name at working directory, in case file not exists with same name it will create a new file and write the content in it. ##############

