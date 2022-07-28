class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.__price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return f"{self.__price} грн"

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError()
        if value < 0:
            raise ValueError()

    @price.deleter
    def price(self):
        self.__price = 0

    def __str__(self):
        return f"{self.name}\nЦена: {self.price}\nОписание: {self.description}, Габариты: {self.dimensions}\n"
