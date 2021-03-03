import unittest
from classes.pub import *
from classes.drink import *
from classes.customer import *

class TestPub(unittest.TestCase):
    def setUp (self):
        self.drink = Drink("rusty nail", 7, 0.8)
        self.pub = Pub("last mans drop", 1000, [self.drink] )
        self.customer_1 = Customer("Bobby Ramshaw", 247.22, 45)

    def test_pub_name(self): 
        self.assertEqual("last mans drop", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(1, len(self.pub.drinks))
    
    def test_find_drink_by_name(self):
        self.assertEqual("rusty nail", self.drink.name)
    
    def test_return_drink_price(self):
        drink = self.pub.find_drink_by_name("rusty nail")
        self.assertEqual(7,drink.price)

    def test_pub_increase_till(self):
        self.pub.increase_till(7)
        self.assertEqual(1007, self.pub.till)

    def test_check_customer_age(self):
        verified = self.pub.check_customer_age(self.customer_1)
        self.assertEqual(None, verified)

    def test_check_customer_drunkenness__starts_zero(self):
        self.assertEqual(0, self.customer_1.drunkenness)

    def test_refuse_customer_drunk(self):
        self.customer_1.buy_drink("rusty nail", self.pub, self.customer_1)
        self.customer_1.buy_drink("rusty nail", self.pub, self.customer_1)
        self.customer_1.buy_drink("rusty nail", self.pub, self.customer_1)
        self.customer_1.buy_drink("rusty nail", self.pub, self.customer_1)
        self.customer_1.buy_drink("rusty nail", self.pub, self.customer_1)
        self.assertEqual(3.2, self.customer_1.drunkenness)
        

