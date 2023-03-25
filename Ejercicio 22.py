__author__ = "Catedra de Algoritmos y Estructuras de datos"

import random

print("\nIngreso de temperaturas")
temp1 = int(input("Ingrese la temperatura 1: "))
temp2 = int(input("Ingrese la temperatura 2: "))
temp3 = int(input("Ingrese la temperatura 3: "))

promedio = (temp1 + temp2 + temp3) / 3

print(f"El promedio de las temperaturas ingresadas fue {promedio} grados")

if temp1 > promedio or temp2 > promedio or temp3 > promedio:
    print("Existe al menos una temperatura que supera al promedio")
else:
    print("Todaslas temperaturas estan por debajo del promedio")