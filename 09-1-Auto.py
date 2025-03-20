class Auto:

    def __init__(self, rekisteri, huippunipeus, tämänhetkinennopeus = 0, matka = 0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunipeus
        self.tämänhetkennopeus = tämänhetkinennopeus
        self.matka = matka

auto = Auto("YHY-789", 220)
print(f"Auton rekisteri on {auto.rekisteri} ja huippunopeus on {auto.huippunopeus}. Tämänhetkennopeus:{auto.tämänhetkennopeus} ja kulijettu matka: {auto.matka}")



