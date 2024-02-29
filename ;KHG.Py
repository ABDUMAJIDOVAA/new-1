def yuridik_inson(kirishlar_nechimarta):
    return 4000 - (kirishlar_nechimarta - 1) * 1000 if kirishlar_nechimarta <= 5 else 1000
def jismoniy_inson(kirishlar_nechimarta):
    return 5000 - (kirishlar_nechimarta - 1) * 1000 if kirishlar_nechimarta <= 7 else 1000
avto = {}
while True:
    avto_raqam = input("sonnio kirit (to`htash ugchun stopni yozing): ").upper()
    if avto_raqam == 'STOP':
        break
    if (avto_raqam):
        if avto_raqam[0] == '0':
            shaxslikning_turi = "Yuridik shaxs"
            narx = jismoniy_inson(len(avto) + 1)
        else:
            shaxslikning_turi = "Jismoniy shaxs"
            narx = yuridik_inson(len(avto) + 1)
        avto[narx] = narx
        print(f"{shaxslikning_turi} moshina uchun  raqam kiritildi. Jami summa: {narx}")
    else:
        print("Noto'g'ri avto raqam formati!")
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


def chek_yuridik_number(number:str) -> bool:
    if isinstance(number, str) and len(number) == 8:
        if (
            (number[:5].isdigit()) & 
            (number[5:].isupper()) & 
            (number[5:].isalpha())
            ):
            return True
    return False

def chek_simple_number(number:str) -> bool:
    if isinstance(number, str) and len(number) == 8:
        if (
            number[:2].isdigit() and 
            number[2].isupper() and 
            number[3:6].isdigit() and 
            number[6:].isupper() and
            number[6:].isalpha()
            ):
            return True
    return False
