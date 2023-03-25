__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("SUELDOS Y AGUINALDO")
print("*" * 80)

total = 0
primero = True
semestre = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio")
for mes in semestre:
    sueldo = float(input(f"Ingrese sueldo de {mes}: "))
    if primero == True:
        may = sueldo
        men = sueldo, mes
        primero = False
    else: 
        if sueldo > may:
            may = sueldo
        if sueldo < men[0]:
            men = sueldo, mes
    total += sueldo

aguinaldo = may / 2
print(f"\nEl aguinaldo es de {aguinaldo}")
print(f"El menor sueldo fue de ${men[0]} y lo obtuvo en el mes de {men[1]}")
promedio = round(total/len(semestre),2)
print(f"El sueldo promedio es de {promedio}")