#we can store multiple items in a single variable using set
myset = {'mango', 'banana', 'orange'}
#set are unorderd,unchangeable, and has no duplicate members
print(myset)
print( len(myset))
#its datatype is set
#because set element are unordered, they return at random when called. so one ca not acces set members
#  by refering to and index or key. but by using a for loop, one can acces set items
for x in myset:
    print(x)
#once a set is created, one can not chane items but rather, can add new items
#to add element,
myset.add('Apple')
print(myset)
#to remove an  element
myset.discard("mango")
print(myset)
