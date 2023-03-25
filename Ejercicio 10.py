__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("COMPLEJO DE CINES")
print("*" * 80)

monto = 0
funciones = 0
funciones_dto = 0

espectadores = int(input("Espectadores (con 0 termina): "))

while espectadores != 0:
    descuento = input("Descuento (S/N): ")
    
    if descuento == "S":
       precio = 50
    else:
        precio = 75
    
    monto = monto + (espectadores * precio)
    
    if descuento == "S":
        funciones_dto += 1
    funciones += 1
    espectadores = int(input("Espectadores (con 0 termina): "))
    
    print("*" * 80)
    print("Recaudacion total$",monto)
    if funciones != 0:
        porc = funciones_dto * 100 / funciones
    else:
        porc = 0
    print("Porcentaje de funciones con descuento: ", porc,"%")
