# Operadores ternarios

# verdadero if condicion else falso

# ejemplo:
edad = 18
print('Es mayor de edad' if edad >= 18 else 'Es menor de edad')

# *args: Permite recibir una cantidad indefinida de argumentos posicionales en forma de tupla
# args es solo un nombre de convención. Se podria poner *numeros, por ejemplo.

# ejemplo:
def suma(*args):
    return sum(args)

print(suma(1, 2, 3))

# **kwargs: Permite recibir una cantidad indefinida de argumentos nombrados (clave-valor), 
# y los guarda como un diccionario.
# kwargs también es un nombre de convención. Se podria poner **datos, por ejemplo

# ejemplo:
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Gabriela", edad=25)


# usandolos juntos:
def ejemplo(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

ejemplo(1, 2, 3, x=10, y=20)
# Imprime:
# 1
# (2, 3)
# {'x': 10, 'y': 20}