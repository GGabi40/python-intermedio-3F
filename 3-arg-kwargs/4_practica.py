# 4. Calcular el promedio de una lista de números usando args y un operador ternario

def promedio(*args):
    total = sum(map(int, args))
    
    return total / len(args) if args else 0

numeros = input('Ingrese numeros separados por espacio: ')
listaNum = numeros.split()

print(promedio(*listaNum))
