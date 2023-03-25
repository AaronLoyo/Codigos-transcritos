__author__ = "Catedra de Algoritmos y Estructuras de Datos"

import random

print("Piedra, Papel o Tijera - Humano vs. Maquina")
print("*" * 80)

humano = input("Ingrese PIEDRA, PAPEL O TIJERA: ")
elementos = ("Piedra", "PAPEL", "TIJERA")
maquina = random.choice(elementos)
print(f"Maquina elige {maquina}")

if humano == maquina:
    resultado = "Empataron"
else:
    if (maquina == "PIEDRA" and humano == "TIJERA") or (maquina == "PAPEL" and humano == "PIEDRA") or (maquina == "TIJERA" and humano == "PAPEL"):
        resultado = "Gana MAQUINA"
    else:
        resultado = "Gana HUMANO"

print(f"!{resultado}¡")