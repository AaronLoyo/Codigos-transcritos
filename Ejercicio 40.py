__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("CENSO POBLACIONAL")
print("*" * 80)

varones = 0
mujeres = 0
escolares = 0
mayor_80 = False

sexo = input("Ingrese sexo (M/F - Otro valor termina): ")

while sexo == "M" or sexo == "F":
    edad = int(input("Ingrese edad: "))
    if sexo == "M":
        varones += 1
    else:
        mujeres += 1
    
    if sexo == "F" and edad >= 4 and edad <= 18:
        escolares += 1
    
    if sexo == "M" and edad > 80:
        mayor_80 = True
    
    sexo = input("Ingrese sexo (M/F - Otro valor termina): ")

print("*" * 80)
if varones > mujeres:
    print("Hay mas varones que mujeres") 

elif mujeres > varones:
    print("Hay mas mujeres que varones")
else:
    print("La cantidad de mujeres y varones es igual")

print(f"Las mujeres en edad escolar son: {escolares}")

if mayor_80 == True:
    print("Hay hombres mayores a 80 años") 
else:
    print("NO hay hombres mayores a 80 años")