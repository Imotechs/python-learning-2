mylist = ['money','rent','mid', 'get']
#add list items using append
mylist.append('Jan')
print(mylist)
#inset list element 
count = len(mylist)
mylist.insert(count,'2022')
print(mylist,count)
#to add two list
secondlist = [count,'counting']
mylist.extend(secondlist)
print(mylist)
#to remove list items using remove,pop and clear mthd
mylist.pop()
print(mylist)
#to nreverse the list
mylist.reverse()
print(mylist)
mylist.remove(mylist[2])
print(mylist)
#the clear() function empties the list completly
mylist.clear()
print(mylist)
#to delet the entire list
del mylist
#print(mylist)
#list compression
list = ['money','rent','mid', 'get']
addedlist = [x for x in list if x in list]

print(addedlist)
#sorting s list
addedlist.sort()
print(addedlist)
#reverse a sorted list
addedlist.sort(reverse=True)
tup = ('money','rent','mid', 'get')
print(f"this  {tup} is a tupple, but this{addedlist} is a List")
