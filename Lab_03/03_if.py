n = int(input("What's n: "))

if n > 0:
    n += 1
elif n < 0:
    n += 2
else:
    n = 10

print(f"Result: {n}")