import unittest
from io import StringIO
import sys

from src.classes import Product, Smartphone, LawnGrass, Category


class TestProductSystem(unittest.TestCase):

    def setUp(self):
        self.product = Product("Продукт1", "Описание", 1000, 5)
        self.smartphone = Smartphone("iPhone", "Смартфон Apple", 99999, 2, "A16", "14 Pro", 256, "black")
        self.grass = LawnGrass("Зеленая", "Газонная трава", 500, 10, "Россия", 14, "зеленый")

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Продукт1")
        self.assertEqual(self.product.description, "Описание")
        self.assertEqual(self.product.price, 1000)
        self.assertEqual(self.product.quantity, 5)

    def test_price_setter_valid(self):
        self.product.price = 1500
        self.assertEqual(self.product.price, 1500)

    def test_price_setter_invalid(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.product.price = -100
        sys.stdout = sys.__stdout__
        self.assertIn("Цена не должна быть нулевая или отрицательная", captured_output.getvalue())

    def test_str_product(self):
        self.assertEqual(str(self.product), "Продукт1, 1000 руб. Остаток: 5 шт.")

    def test_str_smartphone(self):
        expected = "Смартфон iPhone 14 Pro, 256GB, цвет: black, 99999 руб. Остаток: 2 шт."
        self.assertEqual(str(self.smartphone), expected)

    def test_str_lawn_grass(self):
        expected = "Трава Зеленая из Россия, цвет: зеленый, срок прорастания: 14 дней, 500 руб. Остаток: 10 шт."
        self.assertEqual(str(self.grass), expected)

    def test_add_same_type(self):
        p1 = Product("A", "desc", 100, 2)
        p2 = Product("B", "desc", 200, 3)
        result = p1 + p2
        self.assertEqual(result, 100 * 2 + 200 * 3)

    def test_add_different_type(self):
        with self.assertRaises(TypeError):
            _ = self.product + self.smartphone

    def test_add_wrong_type(self):
        with self.assertRaises(TypeError):
            _ = self.product + 123

    def test_new_product_from_dict(self):
        data = {
            'name': 'Тест',
            'description': 'Описание',
            'price': 300,
            'quantity': 4
        }
        p = Product.new_product(data)
        self.assertIsInstance(p, Product)
        self.assertEqual(p.name, 'Тест')
        self.assertEqual(p.price, 300)

    def test_category_add_product(self):
        category = Category("Смартфоны", "Описание категории")
        category.add_product(self.smartphone)
        self.assertIn("Смартфон iPhone", category.products)
        self.assertEqual(str(category), "Смартфоны, количество продуктов: 2 шт.")

    def test_category_add_invalid(self):
        category = Category("Тест", "Ошибка")
        with self.assertRaises(TypeError):
            category.add_product("не продукт")

    def test_category_counter(self):
        self.assertGreaterEqual(Category.category_count, 2)


if __name__ == "__main__":
    unittest.main()