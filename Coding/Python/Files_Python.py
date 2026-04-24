import os
os.chdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice") ##### to change the current working directory to the given path
os.system("ls")

############################# ? with open ("file name", "x") - this will create a new file in case file not exists with same name at working directory, in case file exists with same name it will give error that file already exists. if we want to overwrite the file then we can use "w" mode instead of "x" mode. ##############
#with open("myfile.txt",'x') as my_newFile: 
    ######## !- this will not overwrite the file if file exists with same name at working directory, it will give error that file already exists. if we want to overwrite the file then we can use "w" mode instead of "x" mode.
#with open("myfile_x6.txt",'x') as my_newFile: ##### this will create a new file in case file not exists with same name at working directory, in case file exists with same name it will give error that file already exists.
 #   my_newFile.write("Hey this is new file")
  #  my_newFile.write("Hey it is good to see you")
   # my_newFile.write("Hey Good to see you again")
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


######################### ? with open ("File Name", "r") - this will read the file if file exists with same name at working directory, in case file not exists with same name it will give error that file does not exist. ##############
with open ("myfile.txt", "r") as readfile:
    print(readfile.read())
    readfile.close()

################ ? with open ("File Name", "a") - this will append the content in the file if file exists with same name at working directory, in case file not exists with same name it will create a new file and write the content in it. ##############
with open("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/file_append.txt","a") as new_append:
    new_append.write("\nhi this will append \n")
    new_append.write("hi this will create file if now exists \n")
    os.system("ls")
    with open("file_append.txt","r") as read_append:
        print(read_append.read())
        read_append.close()
        os.system("rm file_append.txt") ##### to remove the file after reading it, this will remove the file from the current working directory, if we do not remove the file then it will take up space in the current working directory and it will also cause confusion because we will have multiple files with same name in the current working directory.

###################### ? Writefile - this will write the content in the file if file exists with same name at working directory, in case file not exists with same name it will create a new file and write the content in it. ##############
print ("Below we are using write/open/read/close file to write the content, open the file, read the file and close the file")
with open("myfile_write.txt", "w") as writefile:
    writefile.write("This is my first line in the file\n")
    writefile.write("This is my second line in the file\n")
    writefile.write("This is my third line in the file\n")

myfile=open('myfile_write.txt') # to open the file
print(myfile.read()) # to read the file, this will read the whole file and print the content of the file, if we want to read line by line then we can use readline() method instead of read() method.
myfile.close()  # to close the file after reading it, it is important to close the file after reading it because it will free up the resources that are being used by the file. if we do not close the file then it will cause memory leak and it will also cause the file to be locked, which means that we will not be able to read or write to the file until we close it.

##################### ? readline() method - this will read the file line by line, it will return the first line of the file and then it will return the second line of the file and so on until it reaches the end of the file. ##############
print("Below we are using readline() method to read the file line by line")
os.system("find . -name 'myfile_write.txt'") ##### to find the file in the current working directory
myfile=open("myfile_write.txt") ##### to open the file
print(myfile.readline()) ############ ! (If we don't open the file first and directly try to read it) ValueError : I/O operation on closed file. because we have closed the file after reading it, so we cannot read the file again until we open it again. if we want to read the file again then we have to open the file again.

print(myfile.readline()) ##### this will read the second line of the file
myfile.close()
#print(myfile.readline()) ##### ! this will give error because we have closed the file after reading it, so we cannot read the file again until we open it again. if we want to read the file again then we have to open the file again. ValueError : I/O operation on closed file.

myfile2=open("myfile_write.txt") ##### to open the file again
print(myfile2.readline()) ##### this will read the first line of the file
print(myfile2.readline()) ##### this will read the second line of the file
print(myfile2.readline()) ##### this will read the third line of the file
myfile2.close() ##### to close the file after reading it    

os.system("pwd") ##### to print the current working directory


