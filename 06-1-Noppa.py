import random


def noppa():
    return random.randint(1, 6)



while True:
    luku = noppa()
    print(f"Nopan luku: {luku}")

    if luku == 6:
        print("Kuutonen tuli! Lopetetaan.")
        break




