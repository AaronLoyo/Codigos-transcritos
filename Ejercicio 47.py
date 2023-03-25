__author__ = "Catedra de Algoritmos y Estructuras de Datos"

n = int(input("Ingrese la cantidad de nros a procesar: "))
contador_positivos = 0
mayor_negativos = 0
suma_positivos = 0

for i in range(n):
    
    print(f"Ingrese el numero {i+1}")
    numero = int(input())
    
    if i == 0:
        menor = numero
    elif i == 1:
        if numero < menor:
            segundoMenor = menor
            menor = numero
        else:
            segundoMenor = numero
    else:
        if numero<menor:
            segundoMenor = menor
            menor = numero
        elif numero < segundoMenor:
            segundoMenor = numero
    
    if numero >= 0:
        contador_positivos +=1
        suma_positivos += numero
    
    else:
        if mayor_negativos == 0:
            mayor_negativos = numero
        elif mayor_negativos < numero:
            mayor_negativos = numero

if contador_positivos != 0:
    promedio = suma_positivos / contador_positivos
else:
    promedio = 0

print(f"El segundo menor es: {segundoMenor}")
print(f"El promedio de los numeros positivos es: {promedio}")
print(f"El mayor de los numeros negativos es: {mayor_negativos}")