class Product:
    name: str
    description: str
    __price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """сеттер для цены с проверкой"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict):
        """создает объект Product из словаря"""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __str__(self):
        """представление объекта Product строкой"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """магический метод сложения для объектов Product"""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("операнд справа должен быть объектом типа Product")


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product):
        """добавление продукта в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("можно добавлять только объекты типа Product")

    @property
    def products(self):
        """возвращает список продуктов строкой"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __str__(self):
        """представление объекта category строке"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, кол-во продуктов: {total_quantity} шт."