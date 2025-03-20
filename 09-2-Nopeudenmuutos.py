
class Auto:

    def __init__(self, rekisteri = "DYF-776", huippunopeus = 220, tämänhetkinennopeus = 0, matka = 0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tämänhetkennopeus = tämänhetkinennopeus
        self.matka = matka

autokiihty1 = Auto(tämänhetkinennopeus= 30)
autokiihty2 = Auto(tämänhetkinennopeus= 70)
autokiihty3 = Auto(tämänhetkinennopeus= 50)
jarrutus = Auto(tämänhetkinennopeus= -200)

print(f"Auton nopeus on {autokiihty3.tämänhetkennopeus}")
print(f"Auton uusi nopeus on {jarrutus.tämänhetkennopeus}")


