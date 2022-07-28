from poligons import area_of_triangle

def get_word(text):
    res = []
    for item in text:
        if "o" in item or "O" in item:
            res.append(item)
    return res

def sort(seq, func):
    res = []
    for item in seq:
        if func(item):
            res.append(item)
    return res

if __name__ == '__main__':

    a = int(input("AB = "))
    b = int(input("BC = "))
    c = int(input("AC = "))
    res = area_of_triangle(a, b, c)
    if res and res > 10:
        print(True)


    text = input()
    text = text.split()
    print(get_word(text))

    a = 6
    b = 3
    res = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - c,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    print(res['*'](a, b))

    print(sort([1, 2, 3, 4, 5], lambda item: item % 2 == 0))
    print(sort([-2, -5, 1, 2, 3, 4, 5], lambda item: item < 0 == 0))
    print(sort([1, 2, 3, 4, 5, 10, 15, 17], lambda item: item > 10 == 0))
