
kWt = int(input("Elektr energiya sarfini kiriting (kWt): "))

if kWt < 0:
    print("Sarf manfiy bo'lishi mumkin emas!")
elif kWt <= 100:
    jami_summa = kWt * 100
    print(f"Tarif: 100 so'm/kWt. Jami to'lov: {jami_summa} so'm")
elif kWt <= 300:
    jami_summa = kWt * 200
    print(f"Tarif: 200 so'm/kWt. Jami to'lov: {jami_summa} so'm")
else:
    jami_summa = kWt * 300
    print(f"Tarif: 300 so'm/kWt. Jami to'lov: {jami_summa} so'm")
