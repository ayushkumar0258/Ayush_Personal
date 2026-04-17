import os
###################### ? - getcwd() ##########################
print(os.getcwd()) ##### to check the current working directory

###################### ? - listdir() ##########################
print(os.listdir()) ##### to check the list of files in the current directory
print(os.listdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python")) ##### to check the list of files in the given directory 

####################### ? - makedirs() - this method is used to created nested directories in one go ##########################
############ below we are creating a new directory directoryTest and inside it we are creating another directory OSTesting in one go using makedirs() method ############
#os.makedirs("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting") #################### to create a new directory 
print(os.listdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest")) ##### to check the list of files in the given directory

######################### ? - mkdir() - this method is used to create a new directory in current directory or at given path #####################
print(os.mkdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/mydir_new")) ##### to create a new directory in given path.

############################ ? - rmdir() - this method is used to remove mentioned directory in the path given ##############
os.rmdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/mydir_new") ##### to remove the directory created in the current directory

########################## ? - remove() - this method is used to remove the file mentioned in the path given ##############
print ("list of file at OStesting path is : ",os.listdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting")) ##### to check the list of files in the given directory
#os.remove("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting/myfile.txt") ##### to remove the file mentioned in the path given
print ("list of file at OStesting path is : ",os.listdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting")) ##### to check the list of files in the given directory after removing the file.
################ !- We can create a file directly using OS operations as this used for directories and system operations only. #####################################
######################### ? -  rename () - this method is uswed to rename the file or directory mentioned in the path given ##############
######## file name renaming.
#os.rename("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting/myfile.txt"        ,       "/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting/myfile_renamed.txt") ##### to rename the file mentioned in the path given
print(" List of file after renaming the file at  :  ",os.listdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting")) ##### to check the list of files in the given directory after renaming the file.

######### directory name renameing
os.rename("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting"        ,       "/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OS_Testing_New") ##### to rename the directory mentioned in the path given
###after rename of directory listing the directories in the given path
print("the list of directories inside the given path is : ", os.listdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest")) ##### to check the list of files in the given directory after renaming the directory.

######################## ? - renames() - this method is used to rename the file or directory mentioned in the path given ##############
