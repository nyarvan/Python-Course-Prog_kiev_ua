from random import randint

if __name__ == '__main__':
    print("Exercise 1:")
    res = ""
    for i in range(0, 101, 7):
        res += str(i) + " "
    print(res)

    print("\nExercise 2:")
    res = 1
    min = 4
    max = 16
    n = int(input("Input number in range 4 < n < 16: "))
    if min <= n <= max:
        for i in range(2, n + 1):
            res *= i
        print("Factorial", n, "is", res)
    else:
        print("Wrong number!")

    print("\nExercise 3:")
    multiplier = 5
    for i in range(1, 11):
        res = i * multiplier
        row = str(i) + " x " + str(multiplier) + " = " + str(res)
        print(row)

    print("\nExercise 4:")
    height = int(input("Height: "))
    width = int(input("Width: "))
    print("*" * width)
    for i in range(height -2):
        print('*', ' ' * (width - 2), '*', sep = '')
    print('*' * width)

    print("\nExercise 5:")
    x = [0, 5, 2, 4, 7, 1, 3, 19]
    print(x)
    res = 0
    for i in range(len(x)):
        if x[i] % 2:
            res += 1
    print("Number of odd digits is", res)

    print("\nExercise 6:")
    count = 4
    x = [randint(1, 10) for i in range(count)]
    y = x + [i * i for i in x]

    print("\nExercise 7:")
    count = 12
    x = [randint(7500, 15000) for i in range(count)]
    print(x)
    avrg = sum(x) / len(x)
    print("Average salary is ", avrg)

    print("\nExercise 8:")
    x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    for row in x:
        print(*row, sep=' ')
    summ = 0
    for row in x:
        summ += sum(row)
    print("Sum of matrix is ", summ)

    print("\nExtra Exercise 1:")
    res = ""
    for n in range(101):
        for i in range(2, n):
            if not n % i:
                break
        else:
            res += str(n) + " "
    print(res)  
    
    print("\nExtra Exercise 2:")
    count = int(input("Input count: "))
    j = 0
    for i in range(count, 0, -2):
        print(' ' * j, '*' * i, sep = '')
        j += 1
    j -= 2
    for i in range(i + 2, count + 1, 2):
        print(' ' * j, '*' * i, sep = '')
        j -= 1

    print("\nExtra Exercise 3:")
    x = [7, 2, 9, 4]
    print(x)
    x = x[::-1]
    print(x)


