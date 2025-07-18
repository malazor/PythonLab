import pandas as pd

def mostrar_promedios_mensuales():
    try:
        # Asegurar que pandas no recorte filas
        pd.set_option('display.max_rows', None)

        # Leer CSV
        df = pd.read_csv('datos.csv', delimiter=';')

        # Convertir tipos
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['bono_us'] = pd.to_numeric(df['bono_us'], errors='coerce').round(4)
        df['msci_pe'] = pd.to_numeric(df['msci_pe'], errors='coerce').round(4)

        # Eliminar filas con datos inválidos
        df = df.dropna(subset=['date', 'bono_us', 'msci_pe'])

        # Establecer 'date' como índice
        df.set_index('date', inplace=True)

        # Calcular promedio mensual
        promedio_mensual = df.resample('M').mean()

        # Mostrar todos los promedios
        print("\n📈 Promedios mensuales completos de 'bonds':")
        print(promedio_mensual)

        return promedio_mensual

    except Exception as e:
        print("Error:", e)

# Ejecutar
mostrar_promedios_mensuales()
