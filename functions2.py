#the return values of functions
def namez(firstname,lastname):
    fullname = firstname +' '+ lastname
    return fullname

footballer = ('Leonel', 'Messi')
print( f' i love a footballer by name:{footballer}')
#with this we can call a function anwhere providing new arguiment at any time.
#making an optional arguiment

def Names(firtname, lastname, midlename = ''):
    fullnames = firtname+ ' '+ lastname+' '+ midlename
    print(fullnames)
Names('Adzembeh','Joshua','Imoter')

#or using if mthd
def Names(firtname, lastname, midlename=''):
    if midlename:
        fullnames = firtname+ ' '+ lastname+' '+ midlename
    else:
        fullnames = firtname+ ' '+ lastname

    print(fullnames)
Names('Adzembeh','Joshua')

#returning a dictionary from a function
def Names(firstname, lastname, midlename = ''):
    fullnames = firstname+ ' '+ lastname+' '+ midlename
    person = {'FirstName:':firstname,'Lastname: ': lastname,'Fullname: ': fullnames }
    print(person)

Names('Adzembeh','Joshua','Imoter')
#we can return any type of data from a function, list,tuple,set,dictionary etc...
# passing list to a function
def greetings(names):
    for name in names:
        print(f'Hello {name.title()}')

names =  ['pauli','theresa','rose']
greetings(names)
