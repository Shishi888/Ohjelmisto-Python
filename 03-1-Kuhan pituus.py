kuhan_pituus = float(input("Mitä on kuhan pituus? "))

if kuhan_pituus < 37:
    print(f"Laskea kuhan takaisin järveen! Pituudesta puutuu {37 - kuhan_pituus:.2f} ")
else:
    print("Poor fish. No ota vaan")


#tai if kuhan_pituus < 37:
         #alamittaisuus =37 - kuhan_pituus
         #print(f"kuhasi on {alamittaisuus} cm lyhyt")