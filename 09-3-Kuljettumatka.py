class Auto:
    def __init__(self, rekisteri="DYF-776", huippunopeus=220):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytys(self, change):

        self.nopeus += change
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kuljetus(self, tunnit):

        self.matka += self.nopeus * tunnit



if __name__ == "__main__":
    auto = Auto("ABC-123", 142)
    print(f"Rekisteritunnus: {auto.rekisteri}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
    print(f"Kuljettu matka: {auto.matka} km")


    auto.kiihdytys(30)
    auto.kiihdytys(70)
    auto.kiihdytys(50)
    print(f"Nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")


    auto.kiihdytys(-200)
    print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")


    auto.kuljetus(1.5)
    print(f"Kuljettu matka 1.5 tunnin jälkeen: {auto.matka} km")