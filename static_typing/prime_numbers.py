# Definiendo si un numero es primo utilizando static typing y mypy --check-untyped-defs
def is_prime(number: int) -> bool:
    count = 0
    for i in range(1, number + 1):
        # if i == number or i == 1:
        #     continue
        # if number%i == 0 or number == 1:
        #     count += 1
        # if count > 0:
        #     break
        if number % i == 0:
            count += 1
        
    return count == 2


def run():
    number: int = int(input("Ingresa un número: "))
    print(is_prime(number))


if __name__ == "__main__":
    run()
