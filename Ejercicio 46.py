__author__ = "Catedra de Algoritmos y Estructuras de Datos"

print("SUELDOS Y AGUINALDO")
print("*" * 80)

total = 0
for mes in range(1,7):
    sueldo = float(input(f"Ingrese sueldo mes {mes}:"))
    if mes == 1:
        may = sueldo
        men = sueldo,1
    else:
        if sueldo > may:
            may = sueldo
        if sueldo < men[0]:
            men = sueldo, mes
    total += sueldo

aguinaldo = may / 2
print(f"\nEl aguinaldo es de {aguinaldo}")
print(f"El menor sueldo fue de {men[0]} y lo obtuvo en el mes {men[1]}")
promedio = round(total/6,2)
print(f"El sueldo promedio es de {promedio}")