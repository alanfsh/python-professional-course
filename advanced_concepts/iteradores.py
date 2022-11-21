# Iteradores
# Un iterable es todo objeto que podemos recorrer con un ciclo (listas, tuplas, diccionarios)

# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter))

# Cuando no quedan datos, la excepción StopIteration es elevada

# El ciclo for en python es solo un alias para referirse a un iterador:

my_list = [1,2,3,4,5]

for element in my_list:
  print(element)

# Lo que es lo mismo:

my_list = [1,2,3,4,5]

# Esto hace el ciclo for
my_iter = iter(my_list)

while True: # ciclo infinito
  try:
    element = next(my_iter)
    print(element)
  except StopIteration: # Cuando no queda ningun elemento
    break

# Ventajas de usar iteradores:
# - Ahorra recursos.
# - Ocupan poca memoria.


# Se puede construir un iterador a partir de una clase:
class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo
  """

  #* Constructor de la clase
  def __init__(self, max = None): #self hace referencia al objeto que se creará con esta clase
    self.max = max

  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0 # Primer número par
    #* Convertir un iterable en un iterador
    return self

  # Método para tener la función "next" de Python
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration # Detiene el iterador