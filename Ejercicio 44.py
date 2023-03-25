__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("SECUENCIA DE IMPARES")
print("=" * 40)

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro: "))

if num1 < num2:
    inicio, fin = num1, num2 + 1
else:
    inicio, fin = num2, num1 + 1

if inicio % 2 == 0:
    inicio += 1

print("Secuencia ascendente")
for num in range(inicio, fin, 2):
    print(num, end=" ")

if num1 > num2:
    inicio, fin = num1, num2 - 1
else:
    inicio, fin = num2, num1 - 1

if inicio % 2 == 0:
    inicio += 1
    
print("\nSecuencia descendente")
for num in range(inicio, fin, -2):
    print(num, end=" ")