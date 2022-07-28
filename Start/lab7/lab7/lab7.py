from math import pi

if __name__ == "__main__":
    for i in range(2, 12):
        res = f"Pi = {pi:.{i}f}"
        print(res)


    text3 = "catcatcatcat"
    pattern = ""
    for i in range(1, len(text3)//2):
        pattern = text3[:i]
        if len(pattern) * text3.count(pattern) == len(text3):
            print(pattern)
            break

    s = "sddsdfdjfsdjkdsjd"
    x = {}
    for item in s:
        #if not x.get[item]:
        x[item] = s.count(item)
    print(x)

    month = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thursday", 5: "Fri", 6: "Sat", 0: "Sun"}
    for i in range(8, 32):
        month[i] = month[i % 7]
    print(month)