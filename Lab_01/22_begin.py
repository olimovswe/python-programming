
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

c = a + b + c
b  = c - a - b
a = c - a - b
c = c - a - b


print(f"A ni qiymati  = {a}")
print(f"B ni qiymati = {b}")
print(f"C ni qiymati = {c}")
