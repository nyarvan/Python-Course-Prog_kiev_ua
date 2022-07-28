class Fraction:
    def __init__(self, num, den):
        if not (isinstance(num, int) or isinstance(den, int)):
            raise TypeError("Введенные значения должны быть целыми числами!")
        if den == 0:
            raise ValueError("Значенатель не может быть равен нулю!")
        if num >= den:
            raise ValueError("Это неправильная дробь!")
        self.num = num
        self.den = den

    def __str__(self):
        return f"Дробь: {self.num}/{self.den}"

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Сравниваеться инстанс класса Fraction!")
        return self.num / self.den == other.num / other.den

    def __neg__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Сравниваеться инстанс класса Fraction!")
        return self.num / self.den != other.num / other.den

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Сравниваеться инстанс класса Fraction!")
        return self.num / self.den > other.num / other.den

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Сравниваеться инстанс класса Fraction!")
        return self.num / self.den < other.num / other.den

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Сравниваеться инстанс класса Fraction!")
        return self.num / self.den >= other.num / other.den

    def __le__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Сравниваеться инстанс класса Fraction!")
        return self.num / self.den <= other.num / other.den

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Дробь должна быть инстансом класса Fraction!")
        if self.den == other.den:
            com_num = self.num + other.num
            return f"{com_num}/{self.den}"
        else:
            com_den = self.den * self.num
            com_num = self.num * other.den + other.num * self.den
            return f"{com_num}/{com_den}"

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Дробь должна быть инстансом класса Fraction!")
        if self.den == other.den:
            com_num = self.num - other.num
            return f"{com_num}/{self.den}"
        else:
            com_den = self.den * self.num
            com_num = self.num * other.den - other.num * self.den
            return f"{com_num}/{com_den}"

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Дробь должна быть инстансом класса Fraction!")
        return f"{self.num * other.num}/{self.den * other.den}"

