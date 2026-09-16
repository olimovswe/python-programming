
num1  = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

count = 0

if num1 > 0:
    count += 1
if num2 > 0:
    count += 1
if num3 > 0:
    count += 1

print(f"Result: {count}")


