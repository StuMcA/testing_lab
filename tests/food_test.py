import unittest
from classes.customer import *
from classes.pub import *
from classes.drink import *
from classes.food import *

class TestFood(unittest.TestCase):

    def setUp (self):
        self.food = Food("bangers and mash", 12.95, 1.5)
    
    def test_food_name(self): 
        self.assertEqual("bangers and mash", self.food.name)
    
    def test_food_has_price(self):
        self.assertEqual(12.95, self.food.price)

    def test_food_rejuvenation_lvl(self):
        self.assertEqual(1.5, self.food.rejuvenation_lvl)