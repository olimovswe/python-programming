ball1 = int(input("Talabaning ballni krting: "))
ball2 = int(input("Talabaning ballni krting: "))
ball3 = int(input("Talabaning ballni krting: "))

katta  = ball1

if katta < ball2:
    katta = ball2

if katta < ball3:
    katta = ball3

print(f"Eng ko'p to'plagan talab balli, {katta} ball")
