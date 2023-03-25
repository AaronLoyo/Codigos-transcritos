__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
# Generador de dirección de Mail
# Entradra:
# Nombre
# Apellido
# Dominio
# Salida:
# Dirección de mail propuesta
print('#' * 30)
print('# ' + 'Generador de Mails' + \
(' ' * (30-(len('Generador de Mails')+5))) + '#')
print('#' * 30)
print('\nIngreso de datos:')
nombre = input('\tNombre : ')
apellido = input('\tApellido: ')
dominio = input('\tDominio : ')
#transformar las cadenas ingresadas en minúscula
# independientemente de cómo se ingresaron.
nombre = nombre.lower()
apellido = apellido.lower()
dominio = dominio.lower()
primera_letra_nombre = nombre[0]
primera_letra_apellido = apellido[0]