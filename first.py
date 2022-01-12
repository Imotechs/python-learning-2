import random
list = ['josh','ken','hope']
for x in list:
    print(x)
list1 =('list','rent')
print(list1)
list.append("Imo")
list.insert(2,"Dema")
print(list)
list.extend(list1)
#print(list)
if 'list' in list:
    print(True)
    ano = []
    for x in list:
        ano.append(x)
        print(ano)

else: 
    print(False)