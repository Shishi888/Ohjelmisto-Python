import random



def heita_noppaa(tahkot):
    return random.randint(1, tahkot)



tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

while True:
    silmaluku = heita_noppaa(tahkojen_maara)
    print(f"Nopan silmäluku: {silmaluku}")

    if silmaluku == tahkojen_maara:
        print(f"Maksimi {tahkojen_maara} tuli! Lopetetaan.")
        break
