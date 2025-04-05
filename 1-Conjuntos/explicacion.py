# Son listas, tuplas o diccionarios.

# creación:
x = {1,2,3,4} # conjunto = { elementos }

print(type(x)) # <class 'set'>

y = set() # conjunto vacío

print(type(y))

# con lista:

lista = {(1,3), 5, 6}
print(lista)

#array = {[1,3], 5, 6}
#print(array) #error -> unshashable type


# conjunto de objeto
diccionario = {
    "nombre": "juan",
    "apellido": "perez"
               }

z=set(diccionario)

print(diccionario) # Todo el diccionario
print(z) # solo las claves "nombre", "apellido"


# agregar y quitar elementos
# .add()
# .discard()
# .remove() -> si no encuentra el elemento, tira KeyError

conjunto = {1,2,3,4,5}
print(conjunto)

conjunto.add(6)
print(conjunto)

conjunto.discard(2)
print(conjunto)


