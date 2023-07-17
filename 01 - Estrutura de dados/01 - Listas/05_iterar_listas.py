carros = ["gol", "celta", "palio"]

# for carro in carros:
#     print(carro)


# for indice, carro in enumerate(carros):
#     print(f"{indice}: {carro}")

# teste = enumerate(carros)
# for i in teste:
#     print(f"{int(i[0])+1} - {i[1]}")

for indice, carro in enumerate(carros):
    print(f"{indice+1}: {carro}")