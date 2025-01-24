hytti = input("Anna hytti luokka (lux, a, b, c): ").upper()
hytti_lux = "LUX on parvekkeellinen hytti yläkannalle"
hytti_a = "Hytti A on ikkunallinen hytti autokannen yläpuolella."
hytti_b = "Hytti B on ikkunaton hytti autokannan yläpuolella."
hytti_c ="Hytti C on ikkunaton hytti autokannan alapuolella."

if hytti =="LUX":
    print(hytti_lux)
elif hytti == "A":
    print(hytti_a)
elif hytti == "B":
    print(hytti_b)
elif hytti == "C":
    print(hytti_c)
else:
    print("Virheellinen hytti luokka.")