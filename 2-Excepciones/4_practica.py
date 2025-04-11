# 4. Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
# FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
# embargo, también intenta crear el archivo si no existe.

def abrir_archivo():
    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)

def crea_archivo():
    with open('archivo.txt', 'w') as arc:
        arc.write('Hola!')
        print('Archivo creado.')

try:
    abrir_archivo()
except FileNotFoundError as f:
    print(f'ERROR: {f}')
    crea_archivo()
except Exception as e:
    print(f'Algo pasó... {e}')