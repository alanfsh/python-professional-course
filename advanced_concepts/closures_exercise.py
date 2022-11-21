# Crear un closure que permita cambiar el divisor de la operacion
# division_by_3(18) = 6
# division_by_5(100) = 20
# division_by_18(54) = 3

def make_division_by(n):
    assert n != 0, "No puedes dividir entre 0"
    assert type(n) == int, "Solo puedes ingresar numeros enteros"

    def division(x): # Funcion nested
        assert type(x) == int or type(x) == float, "Solo puedes ingresar numeros"
        return x / n
    
    return division # Retorna la funcion nested


def run():
    # Utilizando el Closure para crear las funciones divisoras
    division_by_3 = make_division_by(3) # Recuerda el valor 3 de n, deja pendiente X
    division_by_5 = make_division_by(5) # Recuerda el valor 5 de n, deja pendiente X
    division_by_18 = make_division_by(18) # Recuerda el valor 18 de n, deja pendiente X

    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))


if __name__ == "__main__":
    run()