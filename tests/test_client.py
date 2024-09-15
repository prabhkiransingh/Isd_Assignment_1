"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: {Prabhkiran Singh}
Date: {9/15/2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client  
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase):

    def setUp(self):
        self.setup_item = Client(1, "Prabhkiran", "Singh", "PrabhkiranSingh@rrc.ca")
    
    def test_init_valid_inputs_attributes_set(self):
        # Arrange and Act
        client = Client(1, "Prabhkiran", "Singh", "PrabhkiranSingh@rrc.ca")

        # Assert 
        self.assertEqual(client.client_number, 1)
        self.assertEqual(client.first_name, "Prabhkiran")
        self.assertEqual(client.last_name, "Singh")
        self.assertEqual(client.email_address, "PrabhkiranSingh@rrc.ca")

    def test_init_invalid_client_number_valueerror(self):
        # Arrange None

        # Act and Assert 
        with self.assertRaises(ValueError):
            Client("invalid", "Prabhkiran", "Singh", "PrabhkiranSingh@rrc.ca")
        

    def test_init_blank_first_name_valueerror(self):
        # Arrange None

        # Act and Assert 
        with self.assertRaises(ValueError):
            Client(1, "   ", "Singh", "PrabhkiranSingh@rrc.ca")
        

    def test_init_blank_last_name_vlaueerror(self):
        # Arrange None

        # Act and Assert 
        with self.assertRaises(ValueError):
            Client(1, "Prabhkiran", "   ", "PrabhkiranSingh@rrc.ca")
        

    def test_init_invalid_email_valueerror(self):
        # Arrange

        # Act and Assert 
        self.assertEqual(self.setup_item.email_address, "PrabhkiranSingh@rrc.ca")
        client = Client(1, "Prabhkiran", "Singh", "invalid-email") 

    def test_strip_client_number(self):
        # Arrange

        # Act and Assert 
        self.assertEqual(1, self.setup_item.client_number)

    def test_strip_first_name(self):
        # Arrange

        # Act and Assert 
        self.assertEqual("Prabhkiran", self.setup_item.first_name)

    def test_strip_last_name(self):
        # Arrange

        # Act and Assert 
        self.assertEqual("Singh", self.setup_item.last_name)

    def test_valid_email(self):
        # Arrange 

        # Act and Assert 
        self.assertEqual("PrabhkiranSingh@rrc.ca", self.setup_item.email_address)

    def test_str_method(self):
        # Arrange 
        self.setup_item = Client(1, "Prabhkiran", "Singh", "prabhkiransingh@rrc.ca")
        
        # Act and Assert
        expected = "client_number: 1\nfirst_name: Prabhkiran\nlast_name: Singh\nemail_address: prabhkiransingh@rrc.ca"
        self.assertEqual(expected, str(self.setup_item))