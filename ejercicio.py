nombres = []

for x in range(5):
    valor = input("Ingrese los nombres")
    nombres.append(valor)


menora = nombres[0]
for x in range(1, 5):
    if nombres[x] < menora:
        menora = nombres[x]

print("Los nombres ingresados son: ")
print(nombres)
print("El nombre menor en orden alfabeico es: ")
print(menora)
