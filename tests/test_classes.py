import unittest
from src.classes import Product, Category


class TestProductCategory(unittest.TestCase):

    def test_product_with_zero_quantity_raises(self):
        with self.assertRaises(ValueError) as context:
            Product("Товар", "Описание", 100, 0)
        self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен")


    def test_average_price_with_products(self):
        p1 = Product("Товар1", "Описание", 100, 2)
        p2 = Product("Товар2", "Описание", 200, 1)
        category = Category("Электроника", "Разные товары", [p1, p2])
        expected_avg = (100 + 200) / 2
        self.assertEqual(category.middle_price(), expected_avg)


    def test_average_price_with_no_products(self):
        category = Category("Пустая категория", "Без товаров")
        self.assertEqual(category.middle_price(), 0)


    def test_add_product_and_str(self):
        p = Product("Наушники", "Беспроводные", 1500, 5)
        category = Category("Аудио", "Звук")
        category.add_product(p)
        self.assertIn("Наушники", category.products)
        self.assertIn("количество продуктов: 5", str(category))


    def test_addition_of_products(self):
        p1 = Product("Мышка", "Обычная", 500, 2)
        p2 = Product("Мышка", "Обычная", 300, 1)
        total_value = p1 + p2
        expected = 500 * 2 + 300 * 1
        self.assertEqual(total_value, expected)


    def test_addition_type_error(self):
        p = Product("Клавиатура", "Механическая", 2000, 3)
        with self.assertRaises(TypeError):
            _ = p + "not a product"


if __name__ == "__main__":
    unittest.main()