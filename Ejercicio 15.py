__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("Obtener los ultimos digitos de un numero")
numero = int(input("Ingrese un numero: "))

unidad = numero % 10
decenas = numero % 100

print("El ultimo digito del numero", numero, "es", unidad)
print("Los ultimos 2 digitos del numero", numero, "Son", decenas)