class UserInterface:
# pseudocode
# ask the user for its choice of operation
    def basic_math_operations(self):
        print("\033[92mI have here the basic math operations which are the Addition, Subtraction, Multiplication, and Division")
        selection = input("\033[91mPick a basic math operation among these four (+|-|*|/|^): ")
        return selection

# ask the user for two variables to solve
    def var1(self):
        var1 = float(input("\033[92mEnter your first variable number: "))
        return var1

    def var2(self):
        var2 = float(input("\033[91mEnter your second variable number: "))
        return var2

# print the result of the inputs
    '''addition'''
    def sum(self, sum):
        print("\033[94mThe sum of your input is: ", sum)
    '''subtraction'''
    def difference(self, difference):
        print("\033[95mThe difference of your input is: ", difference)
    '''multiplication'''
    def product(self, product):
        print("\033[96mThe product of your input is: ", product)
    '''division'''
    def quotient(self, quotient):
        print("\033[91mThe quotient of your input is: ", quotient)
    def exponent(self, exponent):
        print("\033[92mThe power of your input is: ", exponent)
# once again, ask the user if want to try again or not
    def retry (self):
        option = input("\033[93mNice choice of your operation and numbers! Do you want to try again? (yes, indeed/already satisfied): ")
        return option