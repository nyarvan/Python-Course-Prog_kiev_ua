from table_mul import Table_Mul
from fibonachi import Fibonachi
from my_sequence import My_sequence

if __name__ == "__main__":
    digit = 2
    count = 11
    table = Table_Mul(digit, count)
    for i in range(len(table)):
        print(f"{digit} x {i} = {table[i]}")
    print("\n")
    fibonachi = Fibonachi(11)
    for item in fibonachi:
        print(item)
    print("\n")
    x = My_sequence()
    for i in range(10):
        print(x[i])