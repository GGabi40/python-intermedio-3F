# 3. Escribe un programa que intente acceder a una clave que no existe en un
# diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

dic = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 44
}

try:
    print(dic["color_pelo"])
except KeyError as k:
    print(f'ERROR: No existe la clave {k}')
except Exception as e:
    print(f'ERROR: {e}')