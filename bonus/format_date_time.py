# Fechas formateadas segun region
from datetime import datetime

# Tabla de codigos de formato
# %Y Year
# %m Month
# %d Day
# %H Hour -> 12 hour format
# %I Hour -> 24 hour format
# %M Minute
# %S Seconds
# %p AM or PM

my_datetime = datetime.utcnow() # Con utcnow() utilizamos la hora mundial, no la del equipo local
print(my_datetime)

# Con strftime damos el formato personalizado utilizando la tabla de codigos
my_str = my_datetime.strftime("%d/%m/%Y")
print(f"Formato LATAM: {my_str}")

my_str = my_datetime.strftime("%m/%d/%Y")
print(f"Formato USA: {my_str}")

# Tambien podemos formatear la fecha con un texto personalizado
my_str = my_datetime.strftime("Este es el año %Y") 
print(f"Formato RANDOM: {my_str}")

my_str = my_datetime.strftime("Son las %I:%M:%S %p") # %I se usa para formato de 24 horas, %H para 12 horas
print(f"Hora actual: {my_str}")