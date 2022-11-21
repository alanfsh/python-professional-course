# Los Sets son una coleccion desordenada de elementos unicos e 
# inmutables(no puede contener listas por ejemplo)
# Los sets se definen asi:
from cgi import print_arguments


my_set = {2, 5, 8} # No confundir con la definicion de diccionarios que llevan {llave:clave, llave2:clave2}
print(my_set)

my_set2 = {1, True, False, "Texto"} # Tambien es un set porque nada se repite
print(my_set2)

my_set3 = {1, 1, 3, 4, 5} # en este set, Python elimina un 1 pra que sea unicamente un 1
print(my_set3)

# my_set4 = {[1,2,3], True, "text"} # Esto dara error porque la lista es mutable, por lo tanto no puede estar en el set
# print(my_set4)


# Creando un SET VACIO
empty_set = set() # Esto crea un set vacío
print(type(empty_set)) # Output <class 'set'>

empty_set = {} # Esto crearia un diccionario vacio
print(type(empty_set)) # Output <class 'dict'>


# Haciendo CAST para convertir a SET
my_list = [1, 1, 2, 3, 4, 4, 5] # Esta lista tiene elementos repetidos
my_set = set(my_list) # Hacemos el cast a set, esto elimina los repetidos y conserva solo uno
print(my_set) # Output {1, 2, 3, 4, 5}

my_tuple = ("Hola", "Hola", "Hola", 1) # Esta tupla tiene elementos repetidos
my_set2 = set(my_tuple) # Hacemos el cast a set, esto elimina los repetidos y conserva solo uno
print(my_set2) # Output {1, 'Hola'}

# AÑADIR elementos a un SET
my_set = {1, 2, 3}
my_set.add(4) # Añade un elemento
print(my_set) # Output {1, 2, 3, 4}

# AÑADIR una lista a un SET
my_set.update([3, 4, 5]) # Update añade solo los elementos de la lista que no esten en el set
print(my_set) # Output {1, 2, 3, 4, 5}

# AÑADIR dos estructuras de datos a un SET
my_set.update((1, 7, 2), {8, 2}) # Update añade solo los elementos de la lista y la tupla que no esten en el set
print(my_set) # Output {1, 2, 3, 4, 5, 6, 7, 8}


# ELIMINAR elementos de un SET
my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set) # Output {1, 2, 3, 4, 5, 6, 7}

# Borrar un elemento existente con discard
my_set.discard(1) # Elimina el 1 del set
print(my_set) # Output {2, 3, 4, 5, 6, 7}

# Borrar un elemento existente con remove
my_set.remove(2) # Elimina el 2 del set
print(my_set) # Output {3, 4, 5, 6, 7}

# Borrar un elemento inexistente con discard
my_set.discard(10) # Esto intentara eliminar el 10 del set, como no existe no hace nada
print(my_set) # Output {3, 4, 5, 6, 7}

# Borrar un elemento existente con remove
# my_set.remove(12) # Esto intentara eliminar el 12 del set, como no existe genera un ERROR
print(my_set) # Output KeyError: 12

# LA DIFERENCIA ENTRE DISCARD Y REMOVE ES QUE SI INTENTAMOS ELIMINAR UN ELEMENTO INEXISTENTE
# DISCARD NO HARA NADA Y REMOVE GENERA UN ERROR


# Borrar un elemento ALEATORIO de un SET
my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)

# Eliminar un elemento aleatorio
my_set.pop()
print(my_set) # Output {2, 3, 4, 5, 6, 7}

# Limpiar el set
my_set.clear() # Elimina todo lo que hay dentro del set, lo deja vacio
print(my_set) # set()


