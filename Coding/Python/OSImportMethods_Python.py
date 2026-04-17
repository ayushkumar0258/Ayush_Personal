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
#os.rename("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting"        ,       "/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OS_Testing_New") ##### to rename the directory mentioned in the path given
###after rename of directory listing the directories in the given path
print("the list of directories inside the given path is : ", os.listdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest")) ##### to check the list of files in the given directory after renaming the directory.

######################## ? - renames() - this method is used to rename the file or directory mentioned in the path given ##############
#print("this will rename this file and directories as well toghether : ", os.renames("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/OSTesting/myfile_renamed.txt"        ,       "/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest/AYush_OS_Testing_New/myfile_renamed_again.txt")) ##### to rename the file mentioned in the path given if path not exists it will create that path and then rename the file.
print("the list of directories inside the given path is : ", os.listdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/DirectoryTest")) ##### to check the list of files in the given directory after renaming the file and directory together.

######################### ? - System info - this method is used to get the system information like platform, version, etc. ##############
############################ ? - uname() - this method is used to get the system information like platform, version, etc. ##############
print("the system information is : ", os.uname()) ##### to get the system information like platform, version, etc.          

######################### ? - name() - this method is used to get the name of the operating system dependent module imported. ##############
print("the name of the operating system dependent module imported is : ", os.name) ##### to get the name of the operating system dependent module imported. it will return posix for linux and mac

######################### ? - system(cmd) - for running system commands  ###############################
os.system("ls") ##### to execute the command in the system and return the exit status of the command. it will list the files and directories in the current directory. we can use any command like mkdir, rmdir, etc. as well.
os.system("find . -name 'myfile*'") ##### to find the file with name starting with myfile in the current directory and subdirectories. we can use any command like mkdir, rmdir, etc. as well.
os.system("mkdir -m 777 mydir_os") ##### to create a new directory with permissions 777 in the current directory. we can use any command like mkdir, rmdir, etc. as well.
os.system("rm -rf mydir_os") ##### to remove the directory created in the current directory. we can use any command like mkdir, rmdir, etc. as well.
os.system("cp myfile.txt ./Python/Practice/DirectoryTest/OSTesting/.") ##### to copy the file from current directory to the given directory. we can use any command like mkdir, rmdir, etc. as well.
os.system("mv ./Python/Practice/DirectoryTest/OSTesting/myfile.txt ./Python/Practice/DirectoryTest/OSTesting/myfile_moved.txt") ##### to move the file from current directory to the given directory. we can use any command like mkdir, rmdir, etc. as well.

####################### ? - exists() - this method is used to check whether the file or directory mentioned in the path given exists or not. it will return True if exists and False if not exists. ##############
print("for checking does path is exists or not? : ", os.path.exists("/Users/ayushkumar/Learning/Github1"))
print("for checking does path is exists or not? : ", os.path.exists("/Users/ayushkumar/Learning/Github"))

######################## ? - isfile() - this method is used to check whether the file mentioned in the path given exists or not. it will return True if exists and False if not exists. ##############
print("for checking does file is exists or not? : ", os.path.isfile("/Users/ayushkumar/Learning/Github/Ayush_Personal/Coding/myfile.txt"))
print("for checking does file is exists or not? : ", os.path.isfile("/Users/ayushkumar/Learning/Github/Ayush_Personal/Coding/myfile.txt1"))


###################### ? - isdir() - this method is used to check whether the directory mentioned in the path given exists or not. it will return True if exists and False if not exists. ##############
print("for checking does this is directory or not? : ", os.path.isdir("/Users/ayushkumar/Learning/Github/Ayush_Personal/Coding/myfile.txt"))
print("for checking does this is directory or not? : ", os.path.isdir("/Users/ayushkumar/Learning/Github/Ayush_Personal/Coding"))

########################## ? -getsize() - this method is used to get the size of the file mentioned in the path given. it will return the size of the file in bytes. ##############
print("the size of the file is in bytes: ", os.path.getsize("/Users/ayushkumar/Learning/Github/Ayush_Personal/Coding/myfile.txt"))
