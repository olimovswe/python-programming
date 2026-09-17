

year  = int(input("What is your year? "))

if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} year is a leap")
else:
    print(f"{year} year isn't a leap")
