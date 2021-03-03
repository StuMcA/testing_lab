class Food:
    def __init__(self, name, price, rejuvenation_lvl):

        self.name = name
        self.price = price
        self.rejuvenation_lvl = rejuvenation_lvl

    def decrease_drunkenness_lvl(self, customer, food ):
        customer.drunkenness -= food.rejuvenation_lvl