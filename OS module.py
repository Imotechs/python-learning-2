#importing and using the OS directory. it allow us to interact with the operating 
# sysytem it is a build in module so no need to install it
import os
#importing the datetime library
from datetime import datetime
#print(dir(os))
#to print the curent directory
#print(os.getcwd())
#to change directory, we specify the new directory as
os.chdir('/Users/ImoTechs/Desktop/')
print(os.getcwd())
#lets check the files in our working directory
#print(os.listdir())
#lets creat a new folder on the desktop
os.makedirs('Learning Python')
#print(os.listdir())
#we can also creat a sub directory directly using the makedirs
#os.makedirs("codess/learning")
#print(os.listdir())
 #to remove a file in a directory
#os.removedirs('codess/learning')
#to rename a file
os.rename('Learning Python','coding python')
#getting informations about our files
mod_time = os.stat('coding python').st_mtime
print(datetime.fromtimestamp(mod_time))
# Very Important --> os.makedirs(f'{mod_time } file')
# using os.walk to track files directories///
for dirpath, dirnames,filenames in os.walk('/Users/ImoTechs/Desktop/python'):
    print('current path: ',dirpath)
    print('directories : ', dirnames)
    print('file :', filenames)
    print()
#the walk mathod can be very usefull in creating applications, one can track every location on the os
#the enviroment scanner
print(os.environ.get('HOME'))