from box import Box
from interface import NumberValidator
from interface import Digit
from interface import SubDigit


if __name__ == "__main__":
    print("Exercise 1:")
    box = Box(2, 5, 7)
    print(box.box_volume)

    print("\nExercise 2:")
    box.x = 12
    print(box.x)
    box.y = 6

    print("\nExercise 3:")
    file = open("time.txt")
    res = "".join(file)
    file.flush()
    file.close()
    print(res)

    print("\nAbstract Base Classes")
    digit = Digit(7)
    print(digit)

    print("\nSubClass")
    digit2 = SubDigit(29)
    print(isinstance(digit2, NumberValidator))
    print(digit2)