import abc

class NumberValidator(abc.ABC):
    @abc.abstractmethod
    def validate(self, digit):
        "validate digit"

    @classmethod
    def __subclasshook__(abc_class, cls):
        for sub_class in cls.__mro__:
            for property_name in sub_class.__dict__:
                if property_name == "validate":
                    return True
        return False

class Digit(NumberValidator):
    def __init__(self, digit):
        self.digit = digit

    def validate(self, digit):
        if not isinstance(digit, int):
            raise TypeError()
        i = 2
        while i < digit:
            if digit % i:
                i += 1
            else:
                return False
        return True

    def __str__(self):
        return f"{self.validate(self.digit)}"

class SubDigit:
    def __init__(self, digit):
        self.digit = digit

    def validate(self, digit):
        if not isinstance(digit, int):
            raise TypeError()
        i = 2
        while i < digit:
            if digit % i:
                i += 1
            else:
                return False
        return True

    def __str__(self):
        return f"{self.validate(self.digit)}"


