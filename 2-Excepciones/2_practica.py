# 2. Escribe un programa que intente sumar un número y una cadena. Si se produce un error
# de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

num = int(input('Ingrese un numero: '))
nan = input('Ingrese otro numero: ')

try:
    res = num + nan
    print(res)
except TypeError:
    print(f'Debe introducir números.')