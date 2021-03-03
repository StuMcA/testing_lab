# from classes.drink import *
# from classes.pub import *

class Customer:
    # declare data-types
    name = str
    # initialise Person Class
    def __init__(self, name, wallet):
        self.name = name 
        self.wallet = wallet 

    # function example
        
        # Enter name of drink
        # Find price of that drink

    
        # Check customer can afford drink
    def reduce_cash(self, amount):
        self.cash -= amount
        # If yes

        # Reduce money in wallet
        # Increase money in till

        # If no
        # No drink