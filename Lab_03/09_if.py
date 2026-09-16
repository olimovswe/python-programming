
a = int(input("A: "))
b = int(input("B: "))

# a = 10
# b = 80

if a > b:
    a , b  = b , a

print(f"A: {a}")
print(f"B: {b}")