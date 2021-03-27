import random

numtosimb = ["Piedra", "Papel", "Tijeras"]
resultadoJuego = ["Empate", "Victoria", "Derrota"]

eleccionAI = random.randrange(0,3)
print("""Piedra, papel, tijeras:
1) Piedra
2) Papel
3) Tijeras""")


eleccionUsuario = int(input("Introduzca número: "))-1
if eleccionUsuario < 0 or eleccionUsuario > 2:
    print("Introdució un número no válido.")
    exit(1)

print(f"Usted eligió {numtosimb[eleccionUsuario]}, su oponente, {numtosimb[eleccionAI]}")
print(f"{resultadoJuego[(eleccionUsuario-eleccionAI)%3]}!!!")