__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("Elecciones Presidenciales")

formula1 = input("Ingrese formula lista 1: ")
votos1 = int(input("Ingrese votos lista 1: "))
formula2 = input("Ingrese formula lista 2: ")
votos2 = int(input("Ingrese votos lista 2: "))
formula3 = input("Ingrese formula lista 3: ")
votos3 = int(input("Ingrese votos lista 3: "))


if votos1 > votos2 and votos1 > votos3:
    primero = formula1, votos1
    if votos2 > votos3:
        segundo = formula2, votos2
    else:
        segundo = formula2, votos3
elif votos2 > votos3:
    primero = formula2, votos2
    if votos1 > votos3:
        segundo = formula1, votos1
    else:
        segundo = formula3, votos3
else:
    primero = formula3, votos3
    if votos1 > votos2:
        segundo = formula1, votos1
    else:
        segundo = formula2, votos2


total = votos1 + votos2 +votos3
porcentaje1 = primero[1] *100 /total
if porcentaje1 > 45:
    resultado = "Gano con mas del 45% de los votos " + primero[0]
else:
    diferencia = porcentaje1 - (segundo[1]) * 100 / total
    if porcentaje1 >= 40 and diferencia >= 10:
        resultado = "Gano con 40%: " + primero[0] + \
            " por diferencia de mas de 10 puntos con " + segundo[0]
    else:
        resultado = "Segunda vuelta entre: " + primero[0] + " y " + segundo[0]

print(resultado)
