num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    katta = num1
    kichik = num2
else:
    katta = num2
    kichik = num1

print(f"Kattasi: {katta}")
print(f"Kichigi: {kichik}")