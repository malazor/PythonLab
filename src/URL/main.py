import requests

def verificar_urls(archivo_txt):
    try:
        with open(archivo_txt, 'r') as archivo:
            urls = [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print(f"El archivo '{archivo_txt}' no fue encontrado.")
        return

    print(f"{'URL':<60} {'STATUS'}")
    print("-" * 70)

    for url in urls:
        try:
            respuesta = requests.head(url, timeout=5)
            print(f"{url:<60} {respuesta.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{url:<60} ERROR: {e.__class__.__name__}")

if __name__ == "__main__":
    archivo_input = input("Ingresa el nombre del archivo .txt con las URLs: ").strip()
    verificar_urls(archivo_input)
