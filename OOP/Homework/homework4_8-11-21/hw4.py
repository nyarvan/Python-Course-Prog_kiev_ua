from rectangle import Rectangle
from fraction import Fraction


if __name__ == "__main__":
    print("Exercise 1:")
    rectangle1 = Rectangle(4, 5)
    rectangle2 = Rectangle(3, 9)
    print("Прямоугольник 1: ", rectangle1)
    print("Прямоугольник 2: ", rectangle2)

    print("Прямоугольник 1 == Прямоугольнику 2?")
    print(rectangle1 == rectangle2)
    print("Прямоугольник 1 != Прямоугольнику 2?")
    print(rectangle1 != rectangle2)
    print("Прямоугольник 1 > Прямоугольнику 2?")
    print(rectangle1 > rectangle2)
    print("Прямоугольник 1 < Прямоугольнику 2?")
    print(rectangle1 < rectangle2)
    print("Прямоугольник 1 >= Прямоугольнику 2?")
    print(rectangle1 >= rectangle2)
    print("Прямоугольник 1 <= Прямоугольнику 2?")
    print(rectangle1 <= rectangle2)

    rectangle3 = rectangle1 + rectangle2
    print("Суммарный прямоугольник:", rectangle3)
    n = 5
    result = rectangle1 * n
    print(f"Площадь прямоугольника 1 умноженного на {n} - {result}")
    rectangle2 *= n
    print(f"Площадь прямоугольника 2 умноженного на {n} - {rectangle2}")

    print("\nExercise 2:")
    fraction1 = Fraction(7, 9)
    fraction2 = Fraction(5, 7)
    print(fraction1)
    print(fraction2)

    print(f"{fraction1} == {fraction2}?")
    print(fraction1 == fraction2)
    print(f"{fraction1} != {fraction2}?")
    print(fraction1 != fraction2)
    print(f"{fraction1} > {fraction2}?")
    print(fraction1 > fraction2)
    print(f"{fraction1} < {fraction2}?")
    print(fraction1 < fraction2)
    print(f"{fraction1} >= {fraction2}?")
    print(fraction1 >= fraction2)
    print(f"{fraction1} <= {fraction2}?")
    print(fraction1 <= fraction2)

    print(f"{fraction1} + {fraction2} = {fraction1 + fraction2}")
    print(f"{fraction1} - {fraction2} = {fraction1 - fraction2}")
    print(f"{fraction1} * {fraction2} = {fraction1 * fraction2}")
