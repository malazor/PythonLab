import os
import pandas as pd
from datetime import datetime
import src.yahoo_finance.download.main_download as dl
from time import sleep

# sys.argv[0] es el nombre del script
# sys.argv[1] es el primer parámetro recibido
def bulk_download():
        
        today = datetime.today().date()

        interval = ["1mo", "1wk", "5d", "1d"]

        # Ruta del directorio actual (este script)
        dir_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta del directorio padre (donde está "data")
        parent_dir = os.path.dirname(dir_script)

        # Construye la ruta completa al archivo CSV
        ruta_csv = os.path.join(parent_dir, "tickers.csv")

        # Intenta leer el archivo
        df = pd.read_csv(ruta_csv, sep=";")

        for index, row in df.iterrows():
            print(f"Descargando JSON {row['Ticker']} . . . ")
            dl.save_ticker_info(row['Ticker'])
            sleep(5)
            for body in interval:
               print(f"Descargando {row['Ticker']} con intervalo {str(body)}")
               dl.save_historical_ticker(row['Ticker'], "2000-01-01", today, str(body))
               sleep(5)
            

# 🧪 Ejemplo de uso
if __name__ == "__main__":
    bulk_download()