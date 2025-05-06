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
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает объект Product из словаря"""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __str__(self):
        """Строковое представление объекта Product"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод сложения для объектов Product"""
        if isinstance(other, Product):
            if type(self) is type(other):
                return self.price * self.quantity + other.price * other.quantity
            else:
                raise TypeError("Нельзя складывать товары разных типов")
        raise TypeError("Операнд справа должен быть объектом типа Product")


class Smartphone(Product):
    efficiency: str
    model: str
    memory: int
    color: str

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
    country: str
    germination_period: int
    color: str

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
        """Добавление продукта в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты типа Product или его наследников")

    @property
    def products(self):
        """Возвращает список продуктов в формате строки"""
        return "\n".join(
            f"{product}" for product in self.__products
        )

    def __str__(self):
        """Строковое представление объекта Category"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."