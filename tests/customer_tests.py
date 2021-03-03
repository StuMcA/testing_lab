import unittest
from classes.customer import *


class TestCustomer(unittest.TestCase):
    def setUp (self):
        self.customer = Customer("Bobby Ramshaw", 247.22)
    
    def test_name(self): 
        self.assertEqual("Bobby Ramshaw", self.customer.name ) 

    def test_customer_has_wallet(self):
        self.assertEqual(247.22, self.customer.wallet)