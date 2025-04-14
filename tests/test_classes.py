import pytest
from src.classes import Product, Category


def test_product_creation():
    product = Product("Товар", "Описание", 1000, 5)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 1000
    assert product.quantity == 5


def test_price_getter_and_setter():
    product = Product("Товар", "Описание", 1000, 5)


    product.price = 1500
    assert product.price == 1500


    product.price = 0
    assert product.price == 1500


    product.price = -100
    assert product.price == 1500


def test_product_new_product():
    data = {
        "name": "Товар",
        "description": "Описание",
        "price": 1200,
        "quantity": 3
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Товар"
    assert product.price == 1200
    assert product.quantity == 3


def test_category_creation_and_add_product():
    product1 = Product("Товар 1", "Описание 1", 100, 2)
    product2 = Product("Товар 2", "Описание 2", 200, 4)

    category = Category("Категория", "Описание категории", [product1])
    assert "Товар 1" in category.products
    assert "100 руб." in category.products
    assert "Остаток: 2" in category.products


    category.add_product(product2)
    assert "Товар 2" in category.products
    assert "200 руб." in category.products


def test_add_invalid_product_to_category(capsys):
    category = Category("Категория", "Описание")
    category.add_product("Не продукт")

    captured = capsys.readouterr()
    assert "Можно добавлять только объекты типа Product" in captured.out