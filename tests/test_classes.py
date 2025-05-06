import unittest
from io import StringIO
import sys
from src.classes import Product, Category


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product_data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': 100,
            'quantity': 5
        }
        self.product = Product.new_product(self.product_data)

    def test_product_initialization(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'This is a test product')
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.quantity, 5)

    def test_price_setter(self):
        self.product.price = 150
        self.assertEqual(self.product.price, 150)

        captured_output = StringIO()          # Create StringIO object to capture output
        sys.stdout = captured_output          # Redirect stdout.
        self.product.price = -10              # Call the method.
        sys.stdout = sys.__stdout__           # Reset redirect.
        self.assertEqual(captured_output.getvalue().strip(), "Цена не должна быть нулевая или отрицательная")

    def test_str_method(self):
        self.assertEqual(str(self.product), 'Test Product, 100 руб. Остаток: 5 шт.')

    def test_add_method(self):
        another_product_data = {
            'name': 'Another Product',
            'description': 'This is another test product',
            'price': 200,
            'quantity': 3
        }
        another_product = Product.new_product(another_product_data)
        result = self.product + another_product
        self.assertEqual(result, 1100)  # 100*5 + 200*3 = 1100


class TestCategory(unittest.TestCase):

    def setUp(self):
        # Reset category count before each test
        Category.category_count = 0
        Category.product_count = 0

        self.product1_data = {
            'name': 'Product 1',
            'description': 'Description 1',
            'price': 100,
            'quantity': 5
        }
        self.product2_data = {
            'name': 'Product 2',
            'description': 'Description 2',
            'price': 200,
            'quantity': 3
        }
        self.product1 = Product.new_product(self.product1_data)
        self.product2 = Product.new_product(self.product2_data)
        self.category = Category('Test Category', 'This is a test category', [self.product1, self.product2])

    def test_category_initialization(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.description, 'This is a test category')
        self.assertEqual(len(self.category._Category__products), 2)
        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.product_count, 2)

    def test_add_product_method(self):
        product3_data = {
            'name': 'Product 3',
            'description': 'Description 3',
            'price': 300,
            'quantity': 2
        }
        product3 = Product.new_product(product3_data)
        self.category.add_product(product3)
        self.assertEqual(len(self.category._Category__products), 3)
        self.assertEqual(Category.product_count, 3)

    def test_str_method(self):
        self.assertEqual(str(self.category), 'Test Category, количество продуктов: 8 шт.')

    def test_products_property(self):
        expected_output = (
            "Product 1, 100 руб. Остаток: 5 шт.\n"
            "Product 2, 200 руб. Остаток: 3 шт."
        )
        self.assertEqual(self.category.products, expected_output)


if __name__ == '__main__':
    unittest.main()
