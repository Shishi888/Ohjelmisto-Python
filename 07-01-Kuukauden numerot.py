def vuoden_aika(kuukausi):

    vuodenajat = (
        "talvi", "talvi", "kevät", "kevät", "kevät", "kesä",
        "kesä", "kesä", "syksy", "syksy", "syksy", "talvi"
    )
    return vuodenajat[kuukausi - 1]

kuukausi = int(input("Anna kuukauden numero (1-12): "))
if 1 <= kuukausi <= 12:
    print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan {vuoden_aika(kuukausi)}.")
else:
    print("Virheellinen kuukausi. Anna numero väliltä 1-12.")