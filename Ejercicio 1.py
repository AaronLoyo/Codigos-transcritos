a=int(input("ingrese el numero a: "))
b=int(input("ingrese el numero b: "))
c=int(input("ingrese el numero c: "))

if a>b and a>c:
    may=1
    if b>c:
        med=c
        men = b
elif b>c and b>a:
    may=b
    if c>a:
        med=c
        men=a
    else:
        med=a
        men=c
else:
    may=c
    if b>a:
        med=b
        men=a
    else:
        med=a
        men=b

if men == may % med:
    print("El tercero es igual al resto de la division de los dos primeros")
else:
    print("El tercero NO es igual al resto de la division de los primeros")       