__author__ = "Catedra de Algoritmos y Estructuras de Datos"

import random

print("*" * 40)
print("Simulador de tirada del juego del punto")
print("*" * 40)

puntos_previos = int(input("\nIngrese sus puntos previos: "))

d1 = random.randint(1,6)
print("Dado 1:", d1)

d2 = random.randint(1,6)
print("Dado 2:", d2)

d3 = random.randint(1,6)
print("Dado 3: ", d3)

duplica = False
puntos = 0

if (d1 % 2) == 0 and d1 == d2 and d1 == d3:
    duplica = True
else:
    
    if d1 == 1:
        puntos += 1
    else:
        if d1 == 3:
            puntos +=2
        else:
            if d1 == 5:
                puntos += 4
    
    if d2 == 1:
        puntos += 1
    elif d2 == 3:
        puntos += 2
    elif d2 == 5:
        puntos += 4
    if d3 == 1:
        puntos += 1
    elif d3 == 3:
        puntos *= 2
    elif d3 == 5:
        puntos += 4

puntos_previos += puntos
print(f"\n Puntos obtenidos de esta tirada: {puntos}")
print(f"\n Puntos totales acumulados: {puntos_previos}")

if duplica:
    print("\n Suertudo!!! duplica de puntaje") 
    
print("\n\n Fin!")