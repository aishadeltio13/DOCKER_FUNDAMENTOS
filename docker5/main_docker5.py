import requests

# URL de ejemplo
url = "https://jsonplaceholder.typicode.com/todos/1"

# Hacemos la petición GET
response = requests.get(url)

# Verificamos que la petición fue exitosa
if response.status_code == 200:
    # Convertimos la respuesta JSON a un diccionario de Python
    data = response.json()
    
    # Mostramos los datos obtenidos
    print("Datos obtenidos de la API:")
    print(data)
else:
    print("Error al conectarse a la API:", response.status_code)
