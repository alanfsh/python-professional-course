def decorator(func):
    def wrapper(*args, **kwargs):
        print("La motocicleta seleccionada es: ")
        func(*args, **kwargs)

    return wrapper

@decorator
def motorcycle_type(moto):
    if moto == "honda" or moto == "suzuki" or moto == "yamaha":
        print("japonesa")
    
    if moto == "italika" or moto == "vento" or moto == "carabela":
        print("china")
    
    if moto == "bajaj" or moto == "hero" or moto == "tvs":
        print("india")


def run():
    moto = input("Ingresa una marca: ").lower()
    motorcycle_type(moto)


if __name__ == "__main__":
    run()