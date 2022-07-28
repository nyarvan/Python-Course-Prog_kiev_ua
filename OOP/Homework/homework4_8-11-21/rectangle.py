class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, (float, int)) or isinstance(height, (float, int))):
            raise TypeError("Введенные значения должны быть вещественным числом!")
        if width < 0 or height < 0:
            raise ValueError("Введенные значения должны быть больше 0!")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Ширина - {self.width} см, висота - {self.height}, площадь - {self.get_area()}"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Сравниваються инстансы класса Rectangle!")
        return self.get_area() == other.get_area()

    def __neg__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Сравниваються инстансы класса Rectangle!")
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Сравниваються инстансы класса Rectangle!")
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Сравниваються инстансы класса Rectangle!")
        return self.get_area() < other.get_area()

    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Сравниваються инстансы класса Rectangle!")
        return self.get_area() >= other.get_area()

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Сравниваються инстансы класса Rectangle!")
        return self.get_area() <= other.get_area()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Сравниваються инстансы класса Rectangle!")
        return self.get_area() + other.get_area()

    def __mul__(self, other):
        if not isinstance(other, (float, int)):
            raise TypeError("Множитель должен быть числом!")
        return self.get_area() * other

    def __imul__(self, other):
        if not isinstance(other, (float, int)):
            raise TypeError("Множитель должен быть числом!")
        return self.get_area() * other

