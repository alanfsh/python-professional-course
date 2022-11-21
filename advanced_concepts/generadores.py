# Generadores
# Los generadores son funciones que guardan un estado. 
# Sugar syntax de los iteradores. Es un iterador escrito de forma más simple.
# Sin necesidad de utilizar clases

# Ejemplo:

def my_gen():

  """un ejemplo de generadores"""

  print('Hello world!')
  n = 0
  yield n 
  # yield es exactamente lo mismo que return en un iterador pero detiene la funcion
  # cada vez que se llama a la función, seguirá desde donde se quedó

  print('Hello heaven!')
  n = 1
  yield n

  print('Hello hell!')
  n = 2
  yield n

a = my_gen()
# llamada a funcion -> outputs
print(next(a)) # Hello world!
print(next(a)) # Hello heaven!
print(next(a)) # Hello hell!
print(next(a)) # Eleva StopIteration cuando ya no quedan elementos, con esto se detiene el generador

# Tambien tenemos generator expression -> es como un list comprehension pero mejor, porque
# puede manejar mucha información con mejor rendimiento ya que genera un elemento a la vez.

# Generator expression
my_list = [0,1,4,7,9,10]

my_second_list = [x**2 for x in my_list] # List comprehension -> Lleva corchetes
my_second_gen = (x**2 for x in my_list) # Generator expression -> Lleva parentesis