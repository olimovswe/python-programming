

year  = int(input("What is your year? "))

if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} Kabisa yili")
else:
    print(f"{year} Kabisa yili emas")
