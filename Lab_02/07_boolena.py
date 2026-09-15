a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

result = (a < b and b < c) or (c < b and b < a)


print(result)