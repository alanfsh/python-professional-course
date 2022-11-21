# Utilizando generadores para imprimir la serie de Fibonacci
import time

def fibo_gen(max=None):
    # En cada yield se detiene la funcion y la proxima vez
    # que se itera continua desde ese yield hacia abajo
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if max and counter >= max: # Si se da un numero limite -> rompemos el ciclo y se detiene
            break           
        if counter == 0:
            counter += 1
            yield n1 # Primer numero devuelve 0
        elif counter == 1:
            counter += 1
            yield n2 # Segundo numero devuelve 1
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux # Devuelve el numero actual(suma de los anteriores)


if __name__ == "__main__":
    fibonacci = fibo_gen(8)
    for element in fibonacci:
        print(element)
        time.sleep(0.5) # Delay en segundos