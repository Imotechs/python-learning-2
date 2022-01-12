#tupple can non be eddited, but can be converted to list and back 
mytuple= ("T","q","w","y")
mylist = []
print(mytuple)
#to access individual tuple
count =len(mytuple)
for x in range(count):
    print(mytuple[x])
    mylist.append(mytuple[x])

print(mylist)
#to convert the list back to tuple,
mylist.insert(2,"jojo")
mytuple1 = tuple(mylist)

print(mytuple1)
#we can add two tuples together
readytuple = mytuple1+mytuple
print(readytuple)
#to delet a tuple, use the del function
del mytuple
#print(mytuple)