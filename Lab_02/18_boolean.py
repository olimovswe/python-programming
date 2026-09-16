
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

result = (num1 == num2 or num1 == num3) or (num2 == num3 or num2 == num1)
print(f"Result: {result}")
