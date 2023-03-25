__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("Analisis de Palabra")
print("=" * 80)

palabra = input("Ingrese la palabra a analizar en mayusculas: ")

largo = len(palabra)
ultima_letra = palabra[largo - 1]

Termina_vocal = False

if ultima_letra == "A" or ultima_letra == "e" or ultima_letra == "I" or \
    ultima_letra == "O" or ultima_letra == "U":
    Termina_vocal = True

print("La palabra ingresada tiene una longitud de ", largo, "Letras") 
if Termina_vocal:
    print("La palabra ingresada termina en vocal") 
      
    