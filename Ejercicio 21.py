__author__ = "Catedra de Algoritmos y Estructuras de Datos"
"""""""""""asdadsa"""
print("Jornal de Operario")
print("=" * 80, "\n")

print("Ingreso de Datos")
print("-" * 80)
turno = int(input("Ingrese el turno del operario (1- Diurno, 2- Nocturno): "))
horas = int(input("Ingrese la cantidad de horas trabajadas: "))

if turno == 1:
    total = horas * 35.5
else:
    total = horas * 40.60

print("\nPresentacion de resultados")
print("La empresa le debe pagar al operario un jornal de $", total)