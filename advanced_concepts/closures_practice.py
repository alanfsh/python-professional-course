# Hola 3 S-> HolaHolaHola

def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, "Solo puedes ingresar cadenas de caracteres"
        return string * n

    return repeater


def run():
    repeat_4 = make_repeater_of(4) # Crea una funcion de tipo repeater que recuerda que n = 4, deja pendiente string
    repeat_2 = make_repeater_of(2) # Crea una funcion de tipo repeater que recuerda que n = 2, deja pendiente string

    print(repeat_4("Closures")) # Ejecuta la funcion repeater con n = 4 y string = Closures
    print(repeat_2("Funciona")) # Ejecuta la funcion repeater con n = 2 y string = Funciona
# Con el closure podemos crear muchas funciones a partir de la funcion anidada

if __name__ == "__main__":
    run()

