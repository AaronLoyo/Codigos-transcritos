__author__ = "Catedra Algoritmos y Estructuras de Datos"

print("Ejercicio C - Conversion de distancias")
pies = float(input("Ingrese la distancia en pies que desea converttir"))

yardas = pies / 3
pulgadas = pies * 12
centimetros = pulgadas * 2.54
metros = centimetros / 100

print("En ", pies, " Pies hay", yardas, "yardas")
print(f"En {pies} pies hay {pulgadas} pulgadas")
print(f"En {pies} pies hay {centimetros} centimetros")
print(f"En {pies} pies hay {metros} metros")