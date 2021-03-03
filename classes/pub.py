class Pub:
    # declare data-types
    name = str
    # initialise Person Class
    def __init__(self, name, till, drinks):
        self.name = name 
        self.till = till
        self.drinks = drinks
    
    def increase_till(self, amount):
        self.till += amount
    # function example
    def find_drink_by_name(self, drink_found):
        for drink in self.drinks:
            if drink.name == drink_found:
                return drink
        return None
