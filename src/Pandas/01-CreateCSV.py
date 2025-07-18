import pandas as pd

# Crear un DataFrame simple
datos = {
    'Nombre': ['Ana', 'Luis', 'Pedro','Manuel', 'Antonio'],
    'Edad': [28, 34, 45, 47, 47],
    'Ciudad': ['Lima', 'Cusco', 'Arequipa', 'Junin','Huanuco']
}

df = pd.DataFrame(datos)

# Guardar como CSV
df.to_csv('Pandas/personas.csv', sep=";", index=False)
