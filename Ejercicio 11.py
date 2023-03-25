__author__ = "Catedra de Algoritmos y Estructuras de Datos"

cant_venta = 0
tot_venta = 0
cant_venta1 = 0
cont_venta400 = 0
cont_venta500 = 0
cont_venta600 = 0
hay_menor_50 = False

venta = int(input("Ingrese una cantidad de ventas (negativo para terminar): "))
while venta >= 0:
    
    cant_venta += 1
    tot_venta += venta
    
    if (venta >= 100 and venta <= 300):
        cant_venta1 += 1
    if venta == 400:
        cont_venta400 += 1
    if venta == 600:
        cont_venta600 += 1
    
    if venta < 50:
        hay_menor_50 = True
    
    venta = int(input("Ingrese otra cantidad de ventas:"))
    
    print("La cantidad de ventas ingresadas fueron: ", cant_venta)
    print("El total de ventas ingresadas fue: ", tot_venta)
    print("La cantidad de ventas entre 200 y 300 unidades es: ", cant_venta1)
    print("La cantidad de ventas con 400 unidades es: ", cont_venta400)
    print("La cantidad de ventas con 500 unidades es: ", cont_venta500)
    print("La cantidad de ventas con 600 unidades es: ", cont_venta600)
    
    if hay_menor_50 == True:
        print("Hubo al menos alguna venta con menos de 50 unidades")
    else:
        print("No hubo venta con menos de 50 unidades")