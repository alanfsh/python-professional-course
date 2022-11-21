# "Ana" = "anA" ???

def is_palindrome(word: str) -> bool: # word: str indica que se espera un string, -> bool indica que la funcion devulve un booleano
    word = word.replace(" ", "").lower()
    return word == word[::-1]


def run():
# word = input("Ingresa una palabra: ")
    print(is_palindrome(1001))
    # Para verificar errores de tipado usamos mypy --check-untyped-defs
    # Aqui esperamos un str en la funcion y enviamos un int, mypy regresa el error


if __name__ == "__main__":
    run()