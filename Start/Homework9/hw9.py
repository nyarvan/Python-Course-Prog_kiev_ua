

if __name__ == '__main__':
    print("Exercise 1:")
    first_string = set(input("Input first string: "))
    second_string = set(input("Input second string: "))
    res = set()
    res = first_string.intersection(second_string)
    print(res)

    print("\nExercise 2:")
    first_list = set()
    second_list = set()
    for i in range(0, 100, 3):
        first_list.add(i)
    for i in range(0, 100, 5):
        second_list.add(i)
    print("Числа кратные 3:", first_list)
    print("Числа кратные 5:", second_list)
    res = first_list.intersection(second_list)
    print("Числа которые в обоих множествах:", res)