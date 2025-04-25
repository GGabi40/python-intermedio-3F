# 5. Imprimir un mensaje de error si no se pasan suficientes argumentos

def promedio(*args):
    return (
        sum(map(int, args)) / len(args)
        if(len(args) >= 1)
        else "Error: No se ingresaron suficientes numeros."
    )

numeros = input('Ingrese numeros separados por espacio: ')
listaNum = numeros.split()

print(promedio(*listaNum))
