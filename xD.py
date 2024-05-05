from datetime import datetime, timedelta

# Tiempo inicial: día 1, hora 23
inicio = datetime(year=2024, month=5, day=1, hour=23)

# Cantidad de horas a sumar
horas_adicionales = 6

# Crear un objeto timedelta con las horas adicionales
tiempo_adicional = timedelta(hours=horas_adicionales)

# Sumar el timedelta al tiempo inicial
tiempo_final = inicio + tiempo_adicional

# Mostrar el resultado
print(f"Tiempo inicial: {inicio.strftime('%d-%m-%Y %H:%M:%S')}")
print(f"Tiempo final después de sumar {horas_adicionales} horas: {tiempo_final.strftime('%d-%m-%Y %H:%M:%S')}")
