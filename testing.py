#importing functions from modules
#we can import as many function as posible from a module
from functions import welcome, my_nick
welcome('Joshua')
my_nick('Josliyoung')
#If the name of a function you’re importing might conflict with an existing name in your program or if the function 
# name is long, you can use ashort, unique alias—an alternate name similar to a nickname for the function.
# You’ll give the function this special nickname when you import thefunction
from functions2 import Names as myname
myname('josh','Havertz')
# Syntax ----> "from module_name import function_name as choice name"
#You can also provide an alias for a module name. Giving a module a short
#alias, like p for pizza, allows you to call the module’s functions more quickly.
#Calling p.make_pizza() is more concise than calling pizza.make_pizza():
import functions as f
f.welcome('kenneth')
