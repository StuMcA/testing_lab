from classes.drink import *
from classes.pub import *

class Customer:
    # declare data-types
    name = str
    # initialise Person Class
    def __init__(self, name, wallet, age):
        self.name = name 
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    # Increases drunkenness
    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
    
     # Removes cash from wallet
    def reduce_cash(self, amount):
        self.wallet -= amount
 
    # Buys drink
    def buy_drink(self, drink_name, pub, customer):

        # Checks customer age, exits if underage
        if pub.check_customer_age(customer):
            return "Get oot ya wee bum"

        # Checks customer drunkenness, exits if too high
        if pub.check_drunkenness_level(customer):
            return "Get oot ya bum"

        # Finds drink by name
        drink = pub.find_drink_by_name(drink_name)

        # If can't afford exits function
        if self.wallet < drink.price:
            return None
        
        # Remove cash and add to pub till
        self.reduce_cash(drink.price)
        pub.increase_till(drink.price)

        # Change alcohol level
        self.increase_drunkenness(drink)