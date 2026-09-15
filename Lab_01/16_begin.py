import math

PI = 3.14

S = float(input("Aylananing yuzasi S ni kiriting: "))

R = math.sqrt(S / PI)

d = 2 * R

print(f"Aylananing radiusi R: {round(R, 2)}")
print(f"Aylananing diametri d: {round(d, 2)}")
