

week = input("Hafta kunini krting: ").lower()


jobDay = ("duyshanba" ,"seyshanba", "chorshanba", "payshanba", "juma")
day = ("shanba", "yakshanba")

if week in jobDay:
    print(f"{week}, Ish kuni!")
elif week in day:
    print(f"{week}, Ish kuni emas!)")
else:
    print(f"{week}, bunday hafta kun mavjud emas!")