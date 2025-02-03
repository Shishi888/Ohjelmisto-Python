luvut = []

while True:
    user = input("Anna luku : ")
    if user == "":
        break
    try:
        luku = int(user)
        luvut.append(luku)
    except ValueError:
        print("Syötä kelvollinen kokonaisluku.")


luvut.sort(reverse=True)

print("Viisi suurinta lukua:", luvut[:5])
