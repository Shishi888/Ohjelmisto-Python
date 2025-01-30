yritys = 0
max_yritys = 5

while yritys < max_yritys:

    käyttäjä = (input("Anna käyttäjä tunnus: "))
    salasana = (input("Anna salasana: "))

    if käyttäjä == "Python"and salasana == "Rules":
        print("Tervetuloa!")
        break
    else:
        yritys = yritys + 1

if yritys == max_yritys:
    print("Pääsy evätty!")




