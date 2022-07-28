class InputError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return 'Hello'


class Rectangle:
    def __init__(self, a: int, b):
        if isinstance(a, str):
            a = int(a.replace('см', ''))
        if not (0 < a <= 100 and 0 < b <= 100):
            raise InputError((a, b), 'Invalid a or b')

        self.a = a
        self.b = b

    def get_area(self):
        return self.a*self.b

    def __str__(self):
        return f"Высота - {self.a}, Ширина - {self.b}: Площадь - {self.get_area()}"

if __name__ == "__main__":
    a = input("Введите высоту прямоугольника: ")
    b = int(input("Введите ширину прямоугольника: "))
    try:
        # if a > 100:
        #     raise InputError(a, "Высота должна быть меньше 100")
        # if b > 100:
        #     raise InputError(b, "Ширина должна быть меньше 100")
        rectangle1 = Rectangle(a, b)
    except InputError as err:
        print(err)
    else:
        print(rectangle1)