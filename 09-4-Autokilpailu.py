import random


class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, change):

        self.nopeus += change
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kuljetus(self, tunnit):

        self.matka += self.nopeus * tunnit



if __name__ == "__main__":

    autot = [Auto(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]

    kilpailu = True
    while kilpailu:
        for auto in autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kuljetus(1)

            if auto.matka >= 10000:
                kilpailu = False
                break


    print("\nKilpailun tulokset:")
    print(f"{'Rekisteri':<10} {'Huippunopeus':<15} {'Nopeus':<10} {'Matka':<10}")
    for auto in autot:
        print(f"{auto.rekisteri:<10} {auto.huippunopeus:<15} {auto.nopeus:<10} {auto.matka:<10.1f}")