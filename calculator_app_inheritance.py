# import the existed python program for the reference of new class
from calculator_app import SimpleAppCalculator
# create the new class
class NewFunction(SimpleAppCalculator):
# implement the new function
    def exponent(self, var1, var2):
        exponent = ((var1 + var2))*((var1 + var2))
        return exponent