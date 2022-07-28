from datetime import datetime
import time

def my_sequence(rule: int, n: int):
    """
    The function creates a sequence for the specified rule and the number of sequence elements.
    :param rule: specified rule for create sequence. Rule have three values: 1 - return element of arithmetic
    progression; 2 - return element of geometric progression and default value - return None.
    :param n: the count elements in sequence.
    :return: rule function reference.
    """
    index = 1

    def arithm_seq(a: int | float, d: int | float):
        """
        The function defines rule of arithmetic progression.
        :param a: the first element sequence.
        :param d: the difference of arithmetic progression.
        :return: element of sequence.
        """
        nonlocal index, n
        while index <= n:
            yield a
            index += 1
            a += d

    def geom_seq(b: int | float, q: int | float):
        """
        The function defines rule of geometric progression.
        :param b: the first element sequence.
        :param q: the denominator of geometric progression.
        :return: element of sequence.
        """
        nonlocal index, n
        while index <= n:
            yield b
            index += 1
            b *= q

    match rule:
        case 1:
            return arithm_seq
        case 2:
            return geom_seq
        case _:
            return None

def sequence_fibonachi():
    """
    Function defines sequence of fibonachi.
    :return: The result function reference.
    """
    index = 0
    res = []
    a, b = 0, 1

    def fibonachi(n: int):
        """
        Function return element sequence of fibonachi and append in result list.
        :param n: Count element of sequence.
        :return: result sequence and time of working.
        """
        nonlocal index, res, a, b
        if index < n:
            while index < n:
                res.append(b)
                a, b = b, a + b
                index += 1
                time.sleep(1)
            return res
        else:
            return res

    return fibonachi

def recursive_fibonachi(n: int):
    """
    Recursive function return element of sequence Fibonachi.
    :param n: Number is element of sequence Fibonachi.
    :return: element of sequence Fibonachi.
    """
    if n <= 1:
        return n
    else:
        return (recursive_fibonachi(n-1) + recursive_fibonachi(n - 2))

def func():
    res = {}
    def my_sum(seq):
        nonlocal res
        seq = tuple(seq)
        summa = 0
        if not res.get(seq):
            for item in seq:
                summa += item
            res[seq] = summa
            return res
        else:
            return res
    return my_sum

if __name__ == '__main__':
    print("Exercise 1:")
    seq = []
    rule, n, a, d = 1, 10, 1, 4
    x = my_sequence(rule, n)
    for item in x(a, d):
        seq.append(item)
    print(seq)

    print("\nExercise 2:")
    n = 10
    x = sequence_fibonachi()
    start = datetime.now()
    print(x(n))
    print(x(n))
    stop = datetime.now()
    print(stop - start)

    n = 10
    start = datetime.now()
    res = []
    for item in range(n):
        time.sleep(1)
        res.append(recursive_fibonachi(item))
    print(res)
    res1 = []
    for item in range(n):
        time.sleep(1)
        res1.append(recursive_fibonachi(item))
    print(res1)
    stop = datetime.now()
    print(stop - start)

    print("\nExercise 3:")
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = func()
    print(x(seq))

