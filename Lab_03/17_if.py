
print("--- Do'onimizga xush kelibsiz! ---")
age = int(input("Yoshingizni krting? "))

if age >= 18:
    membership = input("Do'konimiz azosimisiz (y/n)? ").lower().strip()
    if membership == "y":
        print("Tabriklaymiz! Sizga 10% chegirma taqdim etiladi.")
    else:
        print("Siz a'zo emassiz. To'liq narx to'lanadi.")
else:
    print("Yoshingiz 18 dan kichik. To'liq narx to'lanadi.")
