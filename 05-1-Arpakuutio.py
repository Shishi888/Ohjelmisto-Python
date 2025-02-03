import random

lukumaara = int(input("Kuinka monta kertaa heitetään noppa? "))
summa = 0
for i in range(lukumaara):
    silmäluku = random.randint(1, 6)
    summa += silmäluku


print(f"Silmälukujen summa on {summa}")
print(f"Keskimääräinen silmäluku on{summa / lukumaara}")