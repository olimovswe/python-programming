a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

result = (a > 0 and  b <= 0 and c <= 0) or (a <= 0 and b > 0 and c <= 0) or (a <= 0 and b <= 0 and c > 0)
print(result)
