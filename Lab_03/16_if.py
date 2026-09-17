

vazn = float(input("Vazningizni krting kg: "))
boy = float(input("Boyingizni krting (metrda, masalan 1.80): "))

bmi = vazn / (boy * boy)

if bmi < 18.9:
    print(f"{bmi} Kam vazn")
elif bmi < 24.9:
    print(f"{bmi} Oddiy vazn")
elif bmi < 29.9:
    print(f"{bmi} Ortiqcha vazn")
else:
    print(f"{bmi} Semiz")
