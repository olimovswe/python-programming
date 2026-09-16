x = int(input("X = "))
y = int(input("Y = "))

chorak_1 = (x > 0 and y > 0)
chorak_2 = (x < 0 and y > 0)
chorak_3 = (x < 0 and y < 0)
chorak_4 = (x > 0 and y < 0)

print(f"1-chorak: {chorak_1}")
print(f"2-chorak: {chorak_2}")
print(f"3-chorak: {chorak_3}")
print(f"4-chorak: {chorak_4}")
