
tizim_paroli = "Bunker2026"
pin_code = "7777"

urinishlar = 3

while urinishlar > 0:
    password = input("Parolni kiriting: ")
    pin = input("PIN kodni kiriting: ")

    if password == tizim_paroli and pin == pin_code:
        print("Xush kelibsiz! Bunkerdagi maxfiy ma'lumotlar ochildi!")
        break
    else:
        urinishlar -= 1
        print(f"Xato parol yoki PIN kod!")
        if urinishlar > 0:
            print(f"Sizda {urinishlar} ta urinish qoldi.")
else:
    print("Tizim bloklandi! 3 marta noto'g'ri urinish amalga oshirildi.")
    print("Ruxsat berilmadi.")
