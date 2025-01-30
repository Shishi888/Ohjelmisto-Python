import random

oikea_luku = random.randint(1 , 10)


while True:

    arvaus = int(input("Arva luku, 1 ja 10 välillä: "))

    if arvaus > oikea_luku:
        print("Liian suuri luku")
    elif arvaus < oikea_luku:
        print("Liian pieni luku")
    else:
        print("Yaay! Voitit.")
        break



