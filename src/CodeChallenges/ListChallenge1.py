personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Lima"},
    {"nombre": "Luis", "edad": 34, "ciudad": "Arequipa"},
    {"nombre": "María", "edad": 29, "ciudad": "Lima"},
    {"nombre": "Carlos", "edad": 42, "ciudad": "Cusco"},
    {"nombre": "Valeria", "edad": 19, "ciudad": "Lima"},
    {"nombre": "Jorge", "edad": 55, "ciudad": "Arequipa"}
]

size = len(personas)
limenhos = []

for input in personas:
    if input["ciudad"]=="Lima":
        limenhos.append(input)

print(limenhos)