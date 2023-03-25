print("Calculo de polinomio y discriminante ecuacio 2do. grado")
a = float(input("Ingrese el valr de la constante a del polinomio: "))
b = float(input("Ingrese el valor de la constante b del polinomio: "))
c = float(input("Ingrese el valor de la constante c del polinomio: "))
x = float(input("Ingrese el valor de la constante x del polinomio: "))

y = a * (x ** 2) + b * x + c
discriminante = b ** 2 - 4 * a * c

print("El valor del polinomio en el valor de x= ", x, "es:", y)
print("El discriminante del polinomio es: ", discriminante)