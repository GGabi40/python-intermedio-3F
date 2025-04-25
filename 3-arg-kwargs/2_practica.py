# 2. Buscar una palabra en una lista ingresada por teclado usando args y un operador
# ternario

def buscadorDePalabras (palabraBuscada, *args):
    res = 'Encontrada' if palabraBuscada in args else 'No encontrada'
    return res

palabras = input('Ingresa palabras separadas por espacio: ')
lista = palabras.split()

palabra = input('Que palabra desea buscar? ')

print(buscadorDePalabras(palabra, *lista))