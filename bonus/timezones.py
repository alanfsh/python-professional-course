from datetime import datetime
import pytz

cdmx_timezone = pytz.timezone("America/Mexico_City")
cdmx_date = datetime.now(cdmx_timezone)
print(f"CDMX: ", cdmx_date.strftime("%d/%m/%Y, %I:%M:%S %p"))

tokyo_timezone = pytz.timezone("Asia/Tokyo")
tokyo_date = datetime.now(tokyo_timezone)
print(f"Tokyo: ", tokyo_date.strftime("%d/%m/%Y, %I:%M:%S %p"))

# Para ver todas las zonas horarias en pytz
for tz in pytz.all_timezones:
    print(tz)