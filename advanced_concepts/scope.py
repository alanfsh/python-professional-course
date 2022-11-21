# SCOPE (alcance de la función)
# "Una variable solo esta disponible dentro de la region donde fue creada"

 z = 5 # Scope global, todo el programa

 def my_func():
    z = 3 # Scope local my_func()

    def my_other_func():
        z = 2 # Scope local my_other_func()
        print(z) # Imprime z = 2

    my_other_func()

    print(z) # Imprime z = 3

my_func()

print(z) # Imprime z = 5


# z esta definida en diferentes scopes, al ejecutar el programa se imprime lo siguiente:
# 2
# 3
# 5