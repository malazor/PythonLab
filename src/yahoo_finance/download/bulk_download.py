import os
import pandas as pd

# sys.argv[0] es el nombre del script
# sys.argv[1] es el primer parámetro recibido
def bulk_download():

        # Ruta del directorio actual (este script)
        dir_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta del directorio padre (donde está "data")
        parent_dir = os.path.dirname(dir_script)

        # Construye la ruta completa al archivo CSV
        ruta_csv = os.path.join(parent_dir, "download", "input.csv")

        # Intenta leer el archivo
        df = pd.read_csv(ruta_csv, sep=";")

        for index, row in df.iterrows():
            print(f"{row['symbol']} tiene {row['start']} años")
        # print(df)

# 🧪 Ejemplo de uso
if __name__ == "__main__":
    bulk_download()