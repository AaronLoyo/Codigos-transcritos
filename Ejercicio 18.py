__author__ = "Catedra de Algoritmos y Estructuras de Datos"

ADICIONAL_KM = 0.30

print("Costo del boleto de un viaje")
costo_base = float(input("ingrese el costo base del boleto:  "))
kilometros = int(input("Ingrese los kilometros a recorrer: "))

adicional = kilometros * ADICIONAL_KM
costo_total = costo_base + adicional

print("El costo del viaje es ", costo_total)