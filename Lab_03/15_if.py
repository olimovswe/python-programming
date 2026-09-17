
num1  = int(input("Son krting: "))
amal = input("Amal krting (+ - * / ): ")
num2 = int(input("Son krting: "))

if amal == '+':
    print(f"{num1+num2}")
elif amal == '-':
    print(f"{num1-num2}")
elif amal == '*':
    print(f"{num1*num2}")
elif amal == '/':
    if num2 == 0:
        print("Xatolik Nolga bo'lish mumkin emas")
    else:
        print(f"{num1 / num2}")
else:
    print(f"Noto'g'ri amal krtingiz {amal}")









