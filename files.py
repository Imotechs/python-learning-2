import os

os.chdir('/Users/ImoTechs/Desktop/python')
dec = os.getcwd()
print(dec)
f = open('file.txt','r')
print(f.mode)
f.close()
#usind context manangemnet to avoid thrown exceptions
with open('file.txt','r') as f:
    f_contents = f.read()# use readline to read a single line from the file and readlines to read many
    print(f_contents)
#we can also iltrate using for loop
    for line in f:
        print(line) # good practice to serve memory because it does not read all at a time but line by line
#also, with f.read, we can specify the size we want to read at a time given it an argument
with open('file.txt','r') as f:
    file = f.read(500)
    print(f'new:  {file}', end=';')#the end is a separator
#since we don knwo the size of our file lets loop through 
with open('file.txt','r') as f:
    size = 10
    contents = f.read(size)
    while len(contents)>0:
        print(contents, end = '*')
        
        contents = f.read(size)
#we can use the f.seek(), f.tell() and others to read files

#writint to a file
with open('file2.txt','w') as f: # read and write command check...
   # pass to not to anyting
   f.write('Jesus is behind my coding')
   #we can us the seek method here too
   f.seek(1)
   f.write('  ')
with open('names.txt','w') as f:
    pass

