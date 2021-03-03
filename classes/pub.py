from classes.food import *

class Pub:
    # declare data-types
    name = str
    # initialise Person Class
    def __init__(self, name, till, drinks, foods):
        self.name = name 
        self.till = till
        self.drinks = drinks
        self.foods = foods

    def increase_till(self, amount):
        self.till += amount
    # function example
    def find_drink_by_name(self, drink_found):
        for drink in self.drinks:
            if drink.name == drink_found:
                return drink
        return None
        
    def find_food_by_name(self, food_found):
        for food in self.foods:
            if food.name == food_found:
                return food
        return None


    def check_customer_age(self, customer):
        if customer.age < 18:
            return True

    def check_drunkenness_level(self, customer):
        if customer.drunkenness > 3:
            return True
        
    def buy_food(self , food_name , pub_name , customer):
        

        food = self.find_food_by_name(food_name)
        # If can't afford exits function
        if customer.wallet < food.price:
            return None
        
        # Remove cash and add to pub till
        customer.reduce_cash(food.price)
        self.increase_till(food.price)

        # Change alcohol level
        food.decrease_drunkenness_lvl(customer , food )