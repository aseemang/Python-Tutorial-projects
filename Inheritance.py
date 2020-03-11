'''inheritance is where we can define stuff in class, then define another class that inherits
all the attributes of the other class'''

from Chef import Chef

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

#Say we want to make another class to model another type of chef, see chinese chef

from Chinese_Chef import Chinese_Chef

my_Chinese_Chef = Chinese_Chef()
my_Chinese_Chef.make_special_dish()
my_Chinese_Chef.make_fried_rice()

#the problem is having to physically copy and paste to get same functions. Instead we can use inheritance.
#one problem is the special dish is not proper because of inheritance. we can override it by specifying it directly
# in new class