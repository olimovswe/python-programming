
print("Uchburchakning tomonlarini kiriting!")
a = int(input("A tomon: "))
b = int(input("B tomon: "))
c = int(input("C tomon: "))

if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        print("Bu — Teng tomonli uchburchak.")
    elif a == b or a == c or b == c:
        print("Bu — Teng yonli uchburchak.")
    else:
        print("Bu — Turli tomonli uchburchak.")

else:
    print("Bunday tomonlar bilan uchburchak yasab bo'lmaydi!")
