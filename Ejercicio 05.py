__author__ = "Catedra Algoritmos y Estructuras de Datos"

print("Calculo de Descuento en un medicamento")
precio_actual = float(input("Ingrese el precio actual: "))

descuento = precio_actual * 0.35

precio_nuevo = precio_actual - descuento

print("Precio original:", precio_actual)
print("Descuento del 35%:", descuento)
print("Nuevo precio:", precio_nuevo)