#!/usr/bin/env python3

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default weight is 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_stealability(self):
        """Test default stealability value.'"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), "Kinda stealable.")
        self.assertEqual(prod.explode(), "...boom!")


class AcmeReportTests(unittest.TestCase):
    """Making sure our reports are the tops!"""

    def test_default_num_products(self):
        """Making sure correct number of default products"""
        self.products = generate_products()
        self.assertEqual(len(self.products), 30)

    def test_legal_names(self):
        """Making sure are product names are over 21!"""
        self.products = generate_products()
        for prod in self.products:
            name = prod.name.split()
            self.assertIn(name[0], ADJECTIVES)
            self.assertIn(name[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
