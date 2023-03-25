__author__ = "Catedra de Algoritmos y Estructuras de Datos"

modelo = int(input("Ingrese año de fabricacion: "))
tipo = input("Ingrese tipo (P/T/R): ")
antig = 2015 - modelo

if tipo == "P" or tipo == "T":
    if antig < 10:
        impuestos = 200
    elif antig < 20:
        impuestos = 150
    else:
        impuestos = 0
    if tipo == "T":
        impuestos = impuestos + 150
else:
    impuestos = 100 * antig

print(f"El vehiculo debe abonar ${impuestos}")