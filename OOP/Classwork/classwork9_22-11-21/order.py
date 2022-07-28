def converter_valute(currency, rate):
    def func(f):
        def wrapped(*args, **kwargs):
            print(args, kwargs, args[0].name)
            return f'{f(*args, **kwargs) * rate} {currency}'
        return wrapped
    return func

class Order:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    @converter_valute('euro', 1.27)
    def get_price(self):
        return self.price * self.count

