import unittest
from io import StringIO
import sys
from src.classes import Product, Smartphone, LawnGrass, Category


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

    def test_price_setter_valid(self):
        self.product.price = 150
        self.assertEqual(self.product.price, 150)

    def test_price_setter_invalid(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.product.price = -10
        sys.stdout = sys.__stdout__
        self.assertEqual(self.product.price, 100)
        self.assertEqual(captured_output.getvalue().strip(), "Цена не должна быть нулевая или отрицательная")

    def test_str_method(self):
        self.assertEqual(str(self.product), 'Test Product, 100 руб. Остаток: 5 шт.')

    def test_add_method_same_type(self):
        another_product = Product('Another', 'Another product', 200, 3)
        result = self.product + another_product
        self.assertEqual(result, 100 * 5 + 200 * 3)

    def test_add_method_different_type(self):
        smartphone = Smartphone('Phone', 'Smartphone', 1000, 2, 'High', 'ModelX', 128, 'Black')
        with self.assertRaises(TypeError) as context:
            _ = self.product + smartphone
        self.assertEqual(str(context.exception), "Нельзя складывать товары разных типов")

    def test_add_method_invalid_operand(self):
        with self.assertRaises(TypeError) as context:
            _ = self.product + 5
        self.assertEqual(str(context.exception), "Операнд справа должен быть объектом типа Product")


class TestSmartphone(unittest.TestCase):

    def setUp(self):
        self.smartphone = Smartphone('iPhone', 'Smartphone from Apple', 1000, 10, 'High', '14 Pro', 256, 'Purple')

    def test_smartphone_initialization(self):
        self.assertEqual(self.smartphone.name, 'iPhone')
        self.assertEqual(self.smartphone.model, '14 Pro')
        self.assertEqual(self.smartphone.memory, 256)
        self.assertEqual(self.smartphone.color, 'Purple')

    def test_str_method(self):
        self.assertEqual(
            str(self.smartphone),
            'Смартфон iPhone 14 Pro, 256GB, цвет: Purple, 1000 руб. Остаток: 10 шт.'
        )


class TestLawnGrass(unittest.TestCase):

    def setUp(self):
        self.grass = LawnGrass('GreenMix', 'Lawn Grass from USA', 500, 20, 'USA', 30, 'Green')

    def test_lawngrass_initialization(self):
        self.assertEqual(self.grass.name, 'GreenMix')
        self.assertEqual(self.grass.country, 'USA')
        self.assertEqual(self.grass.germination_period, 30)
        self.assertEqual(self.grass.color, 'Green')

    def test_str_method(self):
        self.assertEqual(
            str(self.grass),
            'Трава GreenMix из USA, цвет: Green, срок прорастания: 30 дней, 500 руб. Остаток: 20 шт.'
        )


class TestCategory(unittest.TestCase):

    def setUp(self):
        Category.category_count = 0
        Category.product_count = 0

        self.product1 = Product('Product 1', 'Description 1', 100, 5)
        self.product2 = Product('Product 2', 'Description 2', 200, 3)
        self.category = Category('Test Category', 'Test description', [self.product1, self.product2])

    def test_category_initialization(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.description, 'Test description')
        self.assertEqual(len(self.category._Category__products), 2)
        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.product_count, 2)

    def test_add_product(self):
        product3 = Product('Product 3', 'Description 3', 300, 2)
        self.category.add_product(product3)
        self.assertEqual(len(self.category._Category__products), 3)
        self.assertEqual(Category.product_count, 3)

    def test_add_product_invalid_type(self):
        with self.assertRaises(TypeError) as context:
            self.category.add_product("not a product")
        self.assertEqual(str(context.exception), "Можно добавлять только объекты типа Product или его наследников")

    def test_products_property(self):
        expected_output = (
            "Product 1, 100 руб. Остаток: 5 шт.\n"
            "Product 2, 200 руб. Остаток: 3 шт."
        )
        self.assertEqual(self.category.products, expected_output)

    def test_str_method(self):
        self.assertEqual(str(self.category), 'Test Category, количество продуктов: 8 шт.')


if __name__ == '__main__':
    unittest.main()