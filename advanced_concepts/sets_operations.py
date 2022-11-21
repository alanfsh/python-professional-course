# Se comportan como conjuntos

my_set1 = {2, 3, 4}
my_set2 = {4, 5, 6}

# UNION
my_set3 = my_set1 | my_set2 # Operador union |
print(my_set3) # Output {2, 3, 4, 5, 6}

# INTERSECCION
my_set4 = my_set1 & my_set2 # operador interseccion & lo que esta en ambos sets, lo que comparten ambos sets
print(my_set4) # Output {4}

# DIFERENCIA
my_set5 = my_set1 - my_set2 # operador diferencia - quita del set1 lo que tambien esta en el set2
print(my_set5) # Output {2, 3}

my_set5 = my_set2 - my_set1 # operador diferencia - quita del set2 lo que tambien esta en el set1
print(my_set5) # Output {5, 6}

# DIFERENCIA SIMETRICA
my_set6 = my_set1 ^ my_set2 # operador diferencia simetrica ^ lo contrario a intersección, se quedan los elementos que no estan en ambos sets
print(my_set6) # Output {2, 3, 5, 6}

# Tambien se puede hacer de forma explicita
# set1.union(set2)
# set1.symmetric_difference(set2)
# set1.difference(set2)
# set1.intersection(set2)