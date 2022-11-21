import time

def fibo_gen(max=None):
    n1, n2 = 0, 1
    count = 0
    while not max or count < max:
        yield n1 # Devuelve el valor del numero anterior, no del actual
        count += 1
        n1, n2 = n2, n1 + n2


if __name__ == "__main__":
    fibonacci = fibo_gen(10)
    for element in fibonacci:
        print(element)
        time.sleep(0.25)