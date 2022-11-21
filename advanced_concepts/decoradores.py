# Decoradores
# Función que recibe como parametro otra función, añade cosas y retorna una función diferente
# Se comporta como un closure

def decorador(func):
    def envoltura(): # Envoltura o Wrapper
        print("Lo que se añade a la funcion original")
        func()

    return envoltura


def saludo():
    print("Hola!")


saludo = decorador(saludo) # Llamamos al decorador y agregamos la envoltura --> Esto se sustituye por @Override

saludo()
# Output
# Lo que se añade a la funcion original
# Hola!


# Cuando usamos Python se simplifica la sintaxis al llamar el decorador

def decorador(func):
    def envoltura(): # Envoltura o Wrapper
        print("Lo que se añade a la funcion original")
        func()

    return envoltura

@decorador  # Esto simplifica la sintaxis que envia la funcion y reemplaza lo que hay en la linea 17
def saludo():
    print("Hola!")

saludo() # Llamamos a la funcion que esta asociada al decorador y agregamos la envoltura
# Output
# Lo que se añade a la funcion original
# Hola!