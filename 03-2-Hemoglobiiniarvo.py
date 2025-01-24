sukupuoli = input("Mikä sinun sukupuoli on? ".upper())
hemoglobiini_arvo = int(input("Anna hemoglobiini arvo (g/l) :"))

if sukupuoli == "nainen" and hemoglobiini_arvo > 117 < 175:
    print("Sinun hemoglobiini arvo on normaali.")
elif  sukupuoli == "nainen" and hemoglobiini_arvo < 117:
    print("Sinun hemoglobiiniarvo on alhainen.")
elif sukupuoli == "nainen" and hemoglobiini_arvo > 175:
    print("Sinun hemoglobiiniarvo on korkea.")
elif  sukupuoli == "mies" and hemoglobiini_arvo > 134 < 195:
    print("Sinun hemoglobiiniarvo on normaali.")
elif sukupuoli == "mies" and hemoglobiini_arvo < 134:
    print("Sinun hemoglobiiniarvo on alhainen.")
elif sukupuoli == "mies" and hemoglobiini_arvo > 195:
    print("Sinun hemoglobiiniarvo on korkea.")
else:
    print("Virhe")

