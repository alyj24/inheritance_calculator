# import the existed file for the reference of new module
from UserInterface import user_module

# create the class
class UserInheritance(user_module):
# implement the new method
    def exponent(self, exponent):
        print("\033[95mThe power of your input is: ", exponent")