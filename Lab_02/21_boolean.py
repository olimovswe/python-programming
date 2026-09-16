
num   = int(input("Enter a number: "))

birlar = num % 10
onlar = num // 10 % 10
yuzlar = num // 100 % 10

result = yuzlar < onlar < birlar

print(f"Result: {result}")