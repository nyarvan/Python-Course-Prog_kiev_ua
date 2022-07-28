from descriptor_box import BoxDescriptor
from datetime import datetime

class Box:

    box_volume = BoxDescriptor(20)

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    x, y, z = property(), property(), property()

    @x.getter
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом!")
        time = str(datetime.now())
        file = open("time.txt", "a")
        file.write(f"{time} было присвоенно значение {value} к полю __x\n")
        file.flush()
        file.close()
        self.__x = value

    @x.deleter
    def x(self):
        raise AttributeError("Field cannot delete")

    @y.getter
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом!")
        time = str(datetime.now())
        file = open("time.txt", "a")
        file.write(f"{time} было присвоенно значение {value} к полю __y\n")
        file.flush()
        file.close()
        self.__y = value

    @y.deleter
    def y(self):
        raise AttributeError("Field cannot delete")

    @z.getter
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом!")
        time = str(datetime.now())
        file = open("time.txt", "a")
        file.write(f"{time} было присвоенно значение {value} к полю __z\n")
        file.flush()
        file.close()
        self.__z = value

    @z.deleter
    def z(self):
        raise AttributeError("Field cannot delete")


