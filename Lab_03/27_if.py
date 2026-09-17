
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
    print(f"({a}, {b}, {c}) — barcha sonlar teng")
else:
    if a >= b and a >= c:
        eng_kattasi = a
    elif b >= a and b >= c:
        eng_kattasi = b
    else:
        eng_kattasi = c
    print(f"Eng katta son: {eng_kattasi}")
