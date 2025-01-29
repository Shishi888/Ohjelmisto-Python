karkausvuosi = int(input("Anna karkausvuosi: "))

if karkausvuosi % 4 == 0  or karkausvuosi % 400 == 0:
    print(f"{karkausvuosi} on karkausvuosi")
else:
    print(f"{karkausvuosi} ei ole karkausvuosi")