class Fibonachi:
    def __init__(self, number):
        self.number = number
        self.counter = 0
        self.f1 = 1
        self.f2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter < self.number:
            self.counter = self.f1 + self.f2
            self.f1, self.f2 = self.f2, self.counter
            return self.counter
        else:
            raise StopIteration