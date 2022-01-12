#a python dictionary is a collection of ordered, changeable and does
#  not allow duplicate members
#from collections import OrderedDict
mydict = {
    'Name': "Josua",
    'DOB': 1995,
    'Nick': "Imotechs"
}
print(mydict)
#to add items 
mydict['Color']= 'red'
print(mydict)
#to update an item,
mydict.update({'DOB':1997})
print(mydict)
#to remove an item
mydict.pop('Color')
print(mydict)
#loopint through a dictionary
for x in mydict:
    print(f'{x} : {mydict[x]}')
# or we can also use
for x,y in mydict.items():
    print(x,y)
#by using the popitem, the last item will be removed.
mydict.popitem()
print(mydict)
#we can use the del function tonremove  an item and can also delet a dictionary completly if item is not specify
del mydict['Name']
print(mydict)
#to empty a dictionary, use the clear function
mydict.clear()
print(mydict)
#cascadeed dictionaries
myfamily = {
    'first_son' :{ 'Name':'Kelvin',
    'age':4
    },
    'sec_son':{
        'Name': 'Jerad',
        'age':3
    }
}
for name in myfamily:
         print(name.title())

