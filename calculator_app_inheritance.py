# import the existed python program for the reference of new class
from SimpleAppCalculator import calculator_app
# create the new class
class NewFunction(calculator_app):
# implement the new function
    def exponent(self, var1, var2):
        exponent = var1 ** var2
        return exponent