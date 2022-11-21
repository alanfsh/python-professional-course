import datetime # Modulo utilizado para tiempo, fechas.

my_time = datetime.datetime.now() # Obtiene la fecha actual con horas minutos y segundos
print(my_time) # Output 2022-08-20 01:15:37.545393

my_day = datetime.date.today() # Obtiene la fecha actual
print(my_day) # Output 2022-08-20

print(f"Day: {my_day.day}")  # Acceder a dia
print(f"Month: {my_day.month}") # Acceder a mes
print(f"Year: {my_day.year}") # Acceder a año