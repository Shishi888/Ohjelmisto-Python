def karsi_parittomat(numerot):

    return [num for num in numerot if num % 2 == 0]

testilista = [8, 9, 4, 2, 3, 7, 1, 0]
karsittu_lista = karsi_parittomat(testilista)

print(f"Alkuperäinen lista: {testilista} ")
print(f"Karistettu lista: {karsittu_lista}")