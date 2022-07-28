class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return self.x * self.y * self.z

    def __gt__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        else:
            return self.get_volume() > other.get_volume()

    def __ge__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        else:
            return self.get_volume() >= other.get_volume()

    def __lt__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        else:
            return self.get_volume() < other.get_volume()

    def __le__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        else:
            return self.get_volume() <= other.get_volume()

    def __eq__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        else:
            return self.get_volume() == other.get_volume()

    def __neg__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        else:
            return not self.get_volume() == other.get_volume()



if __name__ == "__main__":
    box1 = Box(2, 5, 9)
    box2 = Box(1, 3, 9)

    print("Box1 > Box2")
    print(box1 > box2)
    print("Box1 >= Box2")
    print(box1 >= box2)
    print("Box1 < Box2")
    print(box1 < box2)
    print("Box1 <= Box2")
    print(box1 <= box2)
    print("Box1 == Box2")
    print(box1 == box2)
    print("Box1 != Box2")
    print(box1 != box2)
