import pytest
from src.classes import Product, Category

@pytest.fixture
def product_1():
    return Product("Телефон", "Смартфон с камерой", 29999.99, 10)


@pytest.fixture
def product_2():
    return Product("Ноутбук", "Игровой ноутбук", 89999.99, 5)


def test_product_initialization(product_1):
    assert product_1.name == "Телефон"
    assert product_1.description == "Смартфон с камерой"
    assert product_1.price == 29999.99
    assert product_1.quantity == 10


def test_category_initialization(product_1, product_2):
    cat = Category("Электроника", "Техника и гаджеты", [product_1, product_2])
    assert cat.name == "Электроника"
    assert cat.description == "Техника и гаджеты"
    assert cat.products == [product_1, product_2]


def test_total_products_and_categories():
    Category.total_categories = 0
    Category.total_products = 0

    p1 = Product("Телевизор", "Большой экран", 49999.99, 3)
    p2 = Product("Колонки", "Аудиосистема", 15999.99, 7)
