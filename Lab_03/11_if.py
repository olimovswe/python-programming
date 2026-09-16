print("--- Haroratni konversiya qilish dasturi ---")
print("Kiritayotgan harorat turingizni tanlang:")
print("1. Selsiy (Celsius)")
print("2. Farengeyt (Fahrenheit)")
print("3. Kelvin")

tanlov  = int(input("Tanlov: "))
harorat = float(input("Harorat qiymatini kiriting: "))

if tanlov == 1:
    farengeyt = (harorat * 9 / 5) + 32
    kelvin = farengeyt + 273.15
    print(f"{harorat} °C = {farengeyt:.2f} °F")
    print(f"{harorat} °C = {kelvin:.2f} K")
elif tanlov == 2:
    selsiy = (harorat - 32) * 5 / 9
    kelvin = selsiy + 273.15
    print(f"{harorat} °F = {selsiy:.2f} °C")
    print(f"{harorat} °F = {kelvin:.2f} K")
elif tanlov == 3:
    selsiy = harorat - 273.15
    farengeyt = (selsiy * 9 / 5) + 32
    print(f"{harorat} K = {selsiy:.2f} °C")
    print(f"{harorat} K = {farengeyt:.2f} °F")
else:
    print("Noto'g'ri tanlov kiritildi!")


