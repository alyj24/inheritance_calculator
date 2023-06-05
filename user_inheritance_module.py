# import the existed file for the reference of new module
from user_module import UserInterface

# create the class
class UserInheritance(UserInterface):
# implement the new method
    def exponent(self, exponent):
        print("\033[95mThe power of your input is: ", exponent)