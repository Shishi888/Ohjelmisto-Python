import random

Kolmenumeroinen_koodi = "".join(str(random.randint(0,9)) for _ in range(3))
Nelinumeroinen_koodi = "".join(str(random.randint(1,6)) for _ in range (4))

print(f"kolmenumeroinen koodi:  {Kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {Nelinumeroinen_koodi}")
