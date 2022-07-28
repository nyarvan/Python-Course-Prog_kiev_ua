from datetime import datetime
import time

def my_filter(seq, predicate):
    for item in seq:
        if predicate(item):
            yield item

def divider():
    def wrapped(digit):
        res, div = {}, []
        if res.get(digit):
            return res.get(digit)
        for i in range(1, digit + 1):
            if not digit % i:
                div.append(i)
        res[digit] = div
        return res
    return wrapped

def count():
    i = 0
    start = datetime.now()
    def func():
        nonlocal start
        nonlocal i
        i += 1
        end = datetime.now()
        diff = end - start
        #start = end
        return i, str(diff)
    return func

class Fibonachi:
    def __init__(self):
        self.a, self.b = 0, 1
        self.i = 0

    def __call__(self, limited):
        if self.i > limited:
            return None
        else:
            self.a, self.b = self.b, self.a + self.b
            self.i += 1
            return self.b



if __name__ == "__main__":

    seq = [1, 2, 3, 4, 5, 6, 7, 8]
    y = my_filter(seq, lambda x: x % 2)
    for item in y:
        print(item)
    a = [item for item in my_filter(seq, lambda x: not x % 2)]
    print(a)
    
    x = divider()
    print(x(81))
    a = count()
    print(a())
    time.sleep(3)
    print(a())
    time.sleep(3)
    print(a())
    time.sleep(3)
    print(a())

    x = Fibonachi()
    for i in range(0, 12):
        print(x(10))
