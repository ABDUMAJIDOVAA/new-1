def yuridik_shaxs(kirishlar_nechimarta):
    return 4000 - (kirishlar_nechimarta - 1) * 1000 if kirishlar_nechimarta <= 5 else 1000
def jismoniy_shaxs(kirishlar_nechimarta):
    return 5000 - (kirishlar_nechimarta - 1) * 1000 if kirishlar_nechimarta <= 7 else 1000
avto = {}
while True:
    avto_raqam = input("Davlat raqamini kiritng (Ish tugaganda 'stop' ni kiriting)=").upper()
    if avto_raqam == 'stop':
        break
    if (avto_raqam):
        if avto_raqam[0] == '0':
            tur = "Yuridik shaxs"
            narx = yuridik_shaxs(len(avto) + 1)
        else:
            tur = "Jismoniy shaxs"
            narx = jismoniy_shaxs(len(avto) + 1)
        avto[narx] = narx
        print(f"{tur} Davlat raqam kiritildi Jami summa: {narx}")
    else:
        print("Davlat raqamni kiritng!")
print(avto_raqam)


umumiy_summa = sum(avto_park.values())
kirgan_avtomobillar_soni = len(avto_park ,tashriflar_soni = len([narx for narx in avto_park.values() if narx > 4000]))
print(
   f"\nXisob-kitob natijalari:"and
     (f"2 Necha dona avtomobil kirgani: {kirgan_avtomobillar_soni}"
       and (f"3 Tashriflar soni: {tashriflar_soni}") and
       (f"1Umumiy summa: {umumiy_summa}")and
         (f"\nXisob-kitob natijalari:") )
        )