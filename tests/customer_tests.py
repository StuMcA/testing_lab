import unittest
from classes.customer import *
from classes.pub import *
from classes.drink import *

class TestCustomer(unittest.TestCase):
    def setUp (self):
        self.customer = Customer("Bobby Ramshaw", 247.22, 45)
        self.drink = Drink("rusty nail", 7, 0.8)
        self.pub = Pub("last mans drop", 1000, [self.drink] , [])
    
    def test_customer_has_name(self): 
        self.assertEqual("Bobby Ramshaw", self.customer.name ) 

    def test_customer_has_wallet(self):
        self.assertEqual(247.22, self.customer.wallet)
    
    def test_customer_reduce_cash(self):
        self.customer.reduce_cash(7)
        self.assertEqual(240.22, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink("rusty nail", self.pub, self.customer)
        self.assertEqual(240.22, self.customer.wallet)
        self.assertEqual(1007, self.pub.till)
        # self.assertEqual(1, self.pub.drink_sold)
        # self.assertEqual(1, self.pet_shop.stock_count())
        # self.assertEqual(1, customer.pet_count()
        
    def test_drunkenness_starts_at_zero(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_increase_drunkenness(self):
        self.customer.buy_drink("rusty nail", self.pub, self.customer)
        self.assertEqual(0.8, self.customer.drunkenness)