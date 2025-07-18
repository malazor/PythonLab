# Agregar segmento como nueva columna de la tabla
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Lima"},
    {"nombre": "Luis", "edad": 34, "ciudad": "Arequipa"},
    {"nombre": "María", "edad": 29, "ciudad": "Lima"},
    {"nombre": "Carlos", "edad": 42, "ciudad": "Cusco"},
    {"nombre": "Valeria", "edad": 19, "ciudad": "Lima"},
    {"nombre": "Jorge", "edad": 55, "ciudad": "Arequipa"}
]
COLUMN = "segmento"
output = []

def obtener_segmento(input):
    if input["edad"] <=17:
        input[COLUMN] = "Menor"
    elif input["edad"] >17 and input["edad"] <30:
        input[COLUMN] = "Joven"
    elif input["edad"] >29 and input["edad"] <60:
        input[COLUMN] = "Adulto"
    elif input["edad"] >59:
        input[COLUMN] = "Adulto mayor"
    return input

for elemento in personas:
    output.append(obtener_segmento(elemento))

print(output)
