from datetime import datetime

def execution_time(func):
    # Cuando decoramos, la funcion wrapper o anidada recibe los argumentos de la funcion a decorar, con *args y **kwargs se garantiza que reciba cualquier cantidad de argumentos
    def wrapper(*args, **kwargs): # Se agrega *args, **kwargs para que se ejecute el wrapper y reciba tambien argumentos de la funcion a decorar, en este caso suma tiene args, y saludo lleva un kwarg
        initial_time = datetime.now()
        func(*args, **kwargs) # *args y **kwargs tambien se pone aqui para trasladar los argumentos que recibe la funcion original
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")

    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

@execution_time
def suma(a, b):
    return a + b

@execution_time
def saludo(nombre="Juan"): # Este es un argumento nombrado --> keyword argument (kwargs) porque define el keyword="clave"
    print("Hola " + nombre)


random_func()
suma(5, 5) # La funcion lleva argumentos posicionales --> (args)
saludo("Pedro")