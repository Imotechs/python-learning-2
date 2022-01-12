

class Resturant():
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def  status(self):
        print(f'{self.name} is open')

    def locations(self):
        print(f'{self.name} is in {self.location}')

    def flavour(self):
        print('food test'+ self.name)

name = input('New resturant')
location = input('Where is it located ?')
new_resturant = Resturant(f'{name}',f' {location}')
new_resturant.status()
new_resturant.locations()

#CREATING INHERITANCE TO A CLASS
class Icecream(Resturant):
    def __init__(self, name, location,flavour):
            super().__init__(name,location)
            self.flavour = flavour
    def flavor(self):
        print('the flavour is '+ self.flavour.title())

ice = Icecream('Robo','Joy','Creams')
ice.flavor()
ice.status()