# CLOSURES
# Cuando una variable que está en un scope superior es recordada por
# una función que está en un scope inferior, aunque el scope superior sea
# eliminado.

# REGLAS:
# Debemos tener una nested function.
# La nested function debe referenciar un valor de un scope superior.
# La función que envuelve a la nested function debe retornarla también.

# Una función contiene a otra
# La función de adentro usa una variable de la función de afuera
# La función de afuera retorna la función de adentro
# Eso es un closure

# una_variable_cualquiera = la_funcion_anidada()
# una_variable_cualquiera() //invocara la función anidada

def make_multiplier(x):

    def multiplier(n): #FUNCION NESTED(ANIDADA)
        return x * n   # X es una referencia a un scope superior, esta en la funcion principal

    return multiplier  # Aqui se devuelve la FUNCION NESTED

times10 = make_multiplier(10) # Se hace uso del closure para crear nuevas variables que contienen la funcion y recuerdan el valor de X dado
times4 = make_multiplier(4)   # Recuerda el valor X = 4, deja pendiente n

print(times10(3)) # times10 recuerda el valor X = 10, y solo le envia el valor de n = 3
print(times4(5))
print(times10(times4(2)))


