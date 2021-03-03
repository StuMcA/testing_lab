import unittest
from classes.drink import *

class TestDrink(unittest.TestCase):

    def setUp (self):
        self.drink = Drink("rusty nail", 7, 0.8)
    
    def test_drink_name(self): 
        self.assertEqual("rusty nail", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(7, self.drink.price)