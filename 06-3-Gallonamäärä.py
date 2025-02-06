def gallon_litroiksi(gallon):
    per_galon = 3.785
    return gallon * per_galon

while True:
    try:
        gallon = float(input("Bensiinin määrä: "))
        if gallon < 0:
            print("Virhe!")
            break
        litra = gallon_litroiksi(gallon)
        print(f"{gallon} gallona on {litra:.2f} litraa.")

    except ValueError:
        print("Virhe! Syötä numero.")




