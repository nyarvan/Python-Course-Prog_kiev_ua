import string

x = input()
for item in string.punctuation:
    x = x.replace(item, ' ')
while '  ' in x:
    x = x.replace('  ', ' ')

res = x.split()
print(*res)
print(len(res))
