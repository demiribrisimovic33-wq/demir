# programprebere tvojo težo
# in planet
# program izračuna tvojo težo na planetu
# teža = gravitacijski pospešek * teža

planet = input ("Vnesi ime planeta (mars, luna, venera, zemlja, neptun, uran, jupiter, saturn)")

teza = float(input("Vnesi svojo težo na zemlji v kg: "))
if planet == "mars":
    gravitacijski_pospešek = 0.38
elif planet == "luna":
    gravitacijski_pospešek = 0.16
elif planet == "venera":
    gravitacijski_pospešek = 8.87
elif planet == "pluton":
    gravitacijski_pospešek = 0.063
elif planet == "uran":
    gravitacijski_pospešek = 0.82
elif planet == "neptun":
    gravitacijski_pospešek = 1.14
elif planet == "merkur":
    gravitacijski_pospešek = 0.38
elif planet == "saturn":
    gravitacijski_pospešek = 0.914

print("na planetu ", planet, " si težki " , teza*gravitacijski_pospešek)