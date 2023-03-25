__author__ = "Catedra de Algoritmos y Estructuras de Datos"

AÑO_ACTUAL = 2023

print("La galeria de arte")
print("Lectura de Datos")
print("=" * 80)

año_obra1 = int(input("Ingrese el año de creacion de la primer obra: "))
año_obra2 = int(input("Ingrese el año de creacion de la segunda obra: "))
año_obra3 = int(input("Ingrese el año de creacion de la tercer obra: "))

renovar_stock = True
if AÑO_ACTUAL - año_obra1 < 10:
    renovar_stock = False

if AÑO_ACTUAL - año_obra2 < 10:
    renovar_stock = False

if AÑO_ACTUAL - año_obra3 < 10:
    renovar_stock = False

son_antiguas = año_obra1 < 1901 and año_obra2 < 1901 and año_obra3 < 1901

if son_antiguas:
    print("Todas las obras de arte son anteriores al siglos XX, son carisimas!!")