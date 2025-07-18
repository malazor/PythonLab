
def main():
    # 
    textoInput = input("Ingrese un texto.")
    # Limpieza de texto
    filter = str.maketrans('', '', '.,!?¿')
    cleanInput = textoInput.translate(filter)

    textoStructured = cleanInput.split(" ")

    masLargo = {"largo":0, "palabra":""}

    for i in textoStructured:
        if len(i)> masLargo["largo"]:
            masLargo["largo"] = len(i)
            masLargo["palabra"] = i

    print("Cadena mas larga: ", masLargo["palabra"])
    print("Largo de la cadena más larga: ", masLargo["largo"])




    

if __name__ == "__main__":
    main()  # Esto debe estar a la misma altura que el bloque if
