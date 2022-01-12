class Dog():
     """A simple attempt to model a dog."""
     def __init__(self,name,age):
         self.name = name
         self.age = age

     def sit(self):
        print(self.name.title() + ' is siting')

     def roll(self):
         print(self.name.title() + ' is rolling')

mydog = Dog('harry',23)
print("My dog's name is " + mydog.name.title() + ".")
print(' and is aged '+str(mydog.age))
mydog.sit() 
mydog.roll()