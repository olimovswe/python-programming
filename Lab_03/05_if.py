num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

countMusbat = 0
countManfiy = 0


if num1 > 0:
    countMusbat += 1
else:
    countManfiy += 1

if num2 > 0:
    countMusbat += 1
else:
    countManfiy += 1

if num3 > 0:
    countMusbat += 1
else:
    countManfiy += 1

print(f"Musbat : {countMusbat}")
print(f"Manfiy: {countManfiy}")


