# Pogoji - IF stavki

starost = 18
# if pogoj:
if (starost >= 18):
    print("Si polnoleten v SLO")
#if: če smo polnoletni v AMERIKI
if (starost >= 21):
    print("Si polnoleten tudi v ameriki")
else:
    print("Nisi polnoleten")

# procente ocene
# odlično, prav dobro, dobro, zadostno. nezadostno

proc = 85
if proc >= 90:
    print("ODLIČNO")
elif proc >= 80:
    print("Prav dobro")
elif proc >= 70:
    print("Dobro")
elif proc >= 50:
    print("Zadostno")
else:
    print("Nezadostno")
# naloga spremje vašo starost
# izpiši čez koliko let boš polnoleten
# prav tako izpišite, če si polnoleten v US

starost = int(input("Koliko si star?"))

DoPol = 18-starost

if DoPol<0:
    print("si polnoleten")
else:
    print("do polnoletnosti ti manjka ", DoPol " let.")