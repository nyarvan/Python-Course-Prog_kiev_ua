from exception import InputErrorPrice
import string

class Product:
    def __init__(self, name, price, description, dimensions):
        if not isinstance(name, str) or not isinstance(description, str) or not isinstance(dimensions, str):
            raise TypeError("Имя, описание или габариты должны быть строкой")
        price = price.split()
        if not (price[0].isdigit() or "-" in price[0]):
            raise ValueError("Цена состоит только из чисел")
        if float(price[0]) < 0:
            raise InputErrorPrice(price[0], "Цена не может быть отрицательным числом")

        self.name = name
        self.price = price[0]
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}\nЦена: {self.price} грн\nОписание: {self.description}, Габариты: {self.dimensions}\n"