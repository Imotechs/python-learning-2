#passing agument to a function
def welcome(user):
    print(f'{user.title()}, you are Welcome')
    print()

welcome('Jessy')
#using positional arguiment or more than one parameters

def favorite_food(food,type):
    print(f'my favorite food is {food}, i enjoy most when {type}')

food = input('your Favourite food is?>>')
type = input(f'Which type of {food}? >>')
#favorite_food(f'{food}',''f'{type}')
#to avoid mixng things up, we use keywards in arguimwnt and shown
favorite_food( type = f'{type}', food=f'{food}')#check even as things are mixed up, python will make it right still\
# we can also use a default value in the arguemnt if we notice many calls are refer to a perticular variable,
def my_nick(nick, place_call='FSTC'):
    print(f'my nick name is {nick}, at {place_call}')

my_nick('Spark')