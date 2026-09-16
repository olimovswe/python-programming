

char = input("Belgining kirting: ").lower()
unli = "aeiou"

if char.isalpha() and len(char) == 1:
    if char in unli:
        print(f"{char} unli harf")
    else:
        print(f"{char} undosh harf")
else:
    print("Iltimos, faqat bitta harf kiriting")