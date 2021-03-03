import unittest
from classes.customer import *
from classes.pub import *
from classes.drink import *

class TestCustomer(unittest.TestCase):
    def setUp (self):
        self.customer = Customer("Bobby Ramshaw", 247.22)
    
    def test_name(self): 
        self.assertEqual("Bobby Ramshaw", self.customer.name ) 

    def test_customer_has_wallet(self):
        self.assertEqual(247.22, self.customer.wallet)
    
    def test_customer_reduce_cash(self):
        self.customer.reduce_cash(7)
        self.assertEqual(240.22, self.customer.wallet)

    def test_buy_drink(self):
        drink = Drink("rusty nail", 7)
        pub = Pub("last mans drop", 1000, [drink])
        self.customer.buy_drink("rusty nail", pub)
        self.assertEqual(240.22, self.customer.wallet)
        self.assertEqual(1007, pub.till)
        # self.assertEqual(1, self.pub.drink_sold)
        # self.assertEqual(1, self.pet_shop.stock_count())
        # self.assertEqual(1, customer.pet_count()
        