def lentoasemat():

    lentoasemat_dict = {}

    while True:
        print("\nValitse toiminto:")
        print("1 - Syötä uusi lentoasema")
        print("2 - Hae lentoasema")
        print("3 - Lopeta")
        valinta = input("Syötä valinta: ")

        if valinta == "1":
            icao = input("Anna lentoaseman ICAO-koodi: ")
            nimi = input("Anna lentoaseman nimi: ")
            lentoasemat_dict[icao] = nimi
            print("Lentoasema tallennettu.")

        elif valinta == "2":
            icao = input("Anna haettava ICAO-koodi: ")
            if icao in lentoasemat_dict:
                print(f"Lentoaseman nimi: {lentoasemat_dict[icao]}")
            else:
                print("Lentoasemaa ei löytynyt.")

        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")



lentoasemat()
