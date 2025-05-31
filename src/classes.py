from abc import ABC, abstractmethod


class PrintMixin:
    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        print(f"Создан объект класса {cls_name} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    name: str
    description: str
    quantity: int
    __price: int

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @abstractmethod
    def __str__(self):
        pass


class Product(PrintMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name=name, description=description, price=price, quantity=quantity)

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            if type(self) is type(other):
                return self.price * self.quantity + other.price * other.quantity
            else:
                raise TypeError("Нельзя складывать товары разных типов")
        raise TypeError("Операнд справа должен быть объектом типа Product")


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"Смартфон {self.name} {self.model}, {self.memory}GB, цвет: {self.color}, "
                f"{self.price} руб. Остаток: {self.quantity} шт.")


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"Трава {self.name} из {self.country}, цвет: {self.color}, "
                f"срок прорастания: {self.germination_period} дней, "
                f"{self.price} руб. Остаток: {self.quantity} шт.")


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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты типа Product или его наследников")

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."