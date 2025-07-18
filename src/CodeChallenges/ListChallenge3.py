# Genera un nuevo diccionario que contenga el número de personas por ciudad.
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Lima"},
    {"nombre": "Luis", "edad": 34, "ciudad": "Arequipa"},
    {"nombre": "María", "edad": 29, "ciudad": "Lima"},
    {"nombre": "Carlos", "edad": 42, "ciudad": "Cusco"},
    {"nombre": "Valeria", "edad": 19, "ciudad": "Lima"},
    {"nombre": "Jorge", "edad": 55, "ciudad": "Arequipa"}
]

output = {}

for element in personas:
    if not (element["ciudad"] in output):
        output[element["ciudad"]]=1
    else:
        output[element["ciudad"]]=output[element["ciudad"]]+1

print(output)
