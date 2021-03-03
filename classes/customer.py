from classes.drink import *
from classes.pub import *

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
        self.wallet -= amount
        # If yes

        # Reduce money in wallet
        # Increase money in till
    def buy_drink(self, drink_name, pub):
        drink = pub.find_drink_by_name(drink_name)
        if self.wallet < drink.price:
            return None
        # self.pets.append(drink)
        # If no
        self.reduce_cash(drink.price)
        pub.increase_till(drink.price)
        # No drink