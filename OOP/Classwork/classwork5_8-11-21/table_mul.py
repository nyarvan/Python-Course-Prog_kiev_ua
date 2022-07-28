class Table_Mul:
    def __init__(self, digit, number):
        if not (isinstance(digit, int) or isinstance(number, int)):
            raise TypeError()
        self.digit = digit
        self.number = number

    def __len__(self):
        return self.number

    def __getitem__(self, index):
        if index < self.number:
            return self.digit * index
        else:
            raise IndexError
