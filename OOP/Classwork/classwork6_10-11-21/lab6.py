def divider(digit):
    div = 1
    while div <= digit:
        if not digit % div:
            yield div
        div += 1

def multiplicity(mult):
    i = 0
    while True:
        yield i*mult
        i += 1

if __name__ == "__main__":
    x = divider(25)
    for item in x:
        print(item)
    print("\n")
    y = multiplicity(10)
    for item in y:
        if item > 250:
            y.close()
            break
        print(item)
