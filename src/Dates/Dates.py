from datetime import datetime, timedelta

# Crear una fecha (fecha actual)
fecha_actual = datetime.now()
print("Fecha actual:", fecha_actual)

# Crear una fecha específica
fecha_especifica = datetime(2025, 1, 15, 12, 0, 0)  # Año, mes, día, hora, minuto, segundo
print("Fecha específica:", fecha_especifica)

# Formatear una fecha (convertir a cadena)
formato = "%d/%m/%Y %H:%M:%S"  # Día/Mes/Año Hora:Minuto:Segundo
fecha_formateada = fecha_actual.strftime(formato)
print("Fecha actual formateada:", fecha_formateada)

# Parsear una fecha desde una cadena
cadena_fecha = "20/02/2025 15:30:00"
fecha_parseada = datetime.strptime(cadena_fecha, formato)
print("Fecha parseada desde cadena:", fecha_parseada)

# Comparar fechas
if fecha_actual < fecha_especifica:
    print("La fecha actual es anterior a la fecha específica.")
else:
    print("La fecha actual es posterior o igual a la fecha específica.")

# Incrementar o reducir días/horas usando timedelta
incremento_dias = timedelta(days=5)  # Incrementar 5 días
nueva_fecha = fecha_actual + incremento_dias
print("Fecha actual + 5 días:", nueva_fecha)

# Restar fechas para calcular diferencia
diferencia = fecha_especifica - fecha_actual
print("Días hasta la fecha específica:", diferencia.days)
print("Segundos totales hasta la fecha específica:", diferencia.total_seconds())

# Obtener partes específicas de una fecha
print("Año:", fecha_actual.year)
print("Mes:", fecha_actual.month)
print("Día:", fecha_actual.day)
print("Hora:", fecha_actual.hour)
print("Minuto:", fecha_actual.minute)
print("Segundo:", fecha_actual.second)
