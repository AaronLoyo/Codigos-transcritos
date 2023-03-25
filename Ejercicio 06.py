__author__ = "Catedra de Algoritmos y Estructuras de Datos"

C = 299792.458

print("Calculo de conversion de masa en energia (Einstein)")
masa = float(input("Ingrese la masa del objeto que desea calcular"))

e = masa * (C ** 2)

print("La energia de la masa ingresada es : ", e)
