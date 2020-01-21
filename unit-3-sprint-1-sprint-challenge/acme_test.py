#!/usr/bin/env python

import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products, PRODUCT_ADJECTIVES, RANDOM_NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_boxing_glove_price(self):
        """Test that the boxing glove SKU's default price is 10."""
        glove = BoxingGlove('Test boxing glove SKU')
        self.assertEqual(glove.price, 10)

    def test_product_methods(self):
        """Test the stealability() and explode() methods' results."""
        prod = Product(name='Test Product', price=3, weight=40, flammability=2)
        self.assertEqual(prod.stealability(), 'Not so stealable...')
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """Additional test methods for Acme products."""

    def test_default_num_products(self):
        """Test that generate_products's (in acme_report) default num is 30."""
        products_list = generate_products()
        self.assertEqual(len(products_list), 30)

    def test_legal_names(self):
        legal_words = PRODUCT_ADJECTIVES + RANDOM_NOUNS
        product_list = generate_products()
        for product in product_list:
            product_name = product.name
            self.assertIn(product_name.split()[0], legal_words)
            self.assertIn(product_name.split()[1], legal_words)


if __name__ == '__main__':
    unittest.main()
