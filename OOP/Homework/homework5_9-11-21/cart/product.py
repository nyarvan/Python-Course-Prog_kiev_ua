class Product:
    def __init__(self, name, price, description, dimensions):
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой!")
        if isinstance(price, (int, float)):
            self.price = price
        if isinstance(price, str):
            price = price.split()
            if "." in price[0]:
                self.price = map(float, price[0])
            else:
                raise ValueError("Неверный формат цены! Цена должна быть в формате х.хх")
        if not (isinstance(description, str) or isinstance(dimensions, str)):
            raise TypeError("Описание и габариты должны быть строкой!")
        self.name = name
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}\nЦена: {self.price}\nОписание: {self.description}, Габариты: {self.dimensions}\n"
