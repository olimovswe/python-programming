a = int(input("A = "))
b = int(input("B = "))

result = (a % 2 != 0 and b % 2 != 0) or (a % 2 == 0 and b % 2 == 0)

print(result)