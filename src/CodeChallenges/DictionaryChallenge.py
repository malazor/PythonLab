personas = {
    "Sofía": 17,
    "Miguel": 22,
    "Lucía": 35,
    "Pedro": 60,
    "Valentina": 12,
    "Andrés": 45
}

for persona, edad in personas.items():
    if edad < 18:
        print(persona," es niño.")
    elif edad >= 18 and edad <=29:
        print(persona," es joven.")
    elif edad >= 30 and edad <=59:
        print(persona," es aulto.")
    elif edad >= 60:
        print(persona," es adulto mayor.")