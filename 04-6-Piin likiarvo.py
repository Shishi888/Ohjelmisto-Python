import random

pisteiden_maara = int(input("Anna arvottavien pisteiden määrä: "))
if pisteiden_maara <= 0:
    print("Pisteiden määrän on oltava positiivinen kokonaisluku.")
else:
    ympyrassa = 0

    for _ in range(pisteiden_maara):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            ympyrassa += 1

    pi_likiarvo = 4 * (ympyrassa / pisteiden_maara)
    print(f"Piin likiarvo {pisteiden_maara} pisteellä: {pi_likiarvo}")
