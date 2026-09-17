
oylik = float(input("Oylik daromatingizni kiriting: "))

if oylik <= 1500:
    print(f"Soliqlar 0%. Qolgan oylik daromad: {oylik:.2f}")
elif oylik <= 3000:
    Soliq = (oylik * 10) / 100
    qolganOylik = oylik - Soliq
    print(f"Soliqlar: {Soliq:.2f}. Qolgan oylik daromad: {qolganOylik:.2f}")
elif oylik <= 5000:
    Soliq = (oylik * 20) / 100
    qolganOylik = oylik - Soliq
    print(f"Soliqlar: {Soliq:.2f}. Qolgan oylik daromad: {qolganOylik:.2f}")
else:
    Soliq = (oylik * 30) / 100
    qolganOylik = oylik - Soliq
    print(f"Soliqlar: {Soliq:.2f}. Qolgan oylik daromad: {qolganOylik:.2f}")
