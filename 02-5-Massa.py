
Leiviskat = float(input("Anna leiviskät: "))
Naulat = float(input("Anna naulat: "))
Luodit = float(input("Anna luodit: "))

Leiviska_grammat = Leiviskat * 20 * 32 * 13.3
Naula_grammat = Naulat * 32 * 13.3
Luoti_grammat = Luodit * 13.3

Total_grammat = Leiviska_grammat + Naula_grammat + Luoti_grammat


Kilogrammat = int(Total_grammat // 1000)
Grammat = Total_grammat % 1000


print("Massa nykymittojen mukaan:")
print(f"{Kilogrammat} kilogrammaa ja {Grammat:.2f} grammaa.")
