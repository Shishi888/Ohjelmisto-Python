luvut = []

while True:
    käyttäjä = input("Anna luku : ")

    if käyttäjä == "":
        break

    try:
       luku = float(käyttäjä)
       luvut.append(luku)
    except ValueError:
        print("Virhe!")

if luvut:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Ei annettu yhtään lukua.")
