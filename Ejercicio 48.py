__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("Analisis de Texto")
print("*" * 80)

letras = 0
palabras = 0
pals = 0
tieneSA = False
PalSA =  0
cl = 0

ant = None
act = None
while act != ".":
    act = input("Ingrese caracter (con . termina): ")
    if (act == " " or act == ".") and ant != None:
        if cl> 0:
            palabras += 1
            if ant == "s":
              pals += 1
            if tieneSA == True:
                PalSA += 1
            tieneSA = False
            cl = 0
    else:
        letras += 1
        cl += 1
    ant = act

print("*" * 80)
if palabras == 0:
    prom = 0
else:
    prom = letras / palabras
    
print("El promedio de letras por palabra es", prom)
print(f"Las palabras terminadas en S son {pals}")
print(f"Las palabras con la expresion SA son {PalSA}")
print(f"cant. Palabras {palabras}")         