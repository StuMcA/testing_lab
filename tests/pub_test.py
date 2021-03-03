import unittest
from classes.pub import *
from classes.drink import *

class TestPub(unittest.TestCase):
    def setUp (self):
        drink = Drink("rusty nail", 7)
        self.pub = Pub("last mans drop", 1000, [drink] )

    def test_pub_name(self): 
        self.assertEqual("last mans drop", self.pub.name)
    
    def test_pub_has_till(self):
    
        self.assertEqual(1000, self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(1, len(self.pub.drinks))
    
    def test_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("rusty nail")
        self.assertEqual("rusty nail", drink.name)
    
    def test_return_drink_price(self):
       drink = self.pub.find_drink_by_name("rusty nail")
       self.assertEqual(7,drink.price)
       