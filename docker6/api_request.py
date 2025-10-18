import requests

url= "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)


try:
    if response.status_code == 200:
        data = response.json()
        
        print("Datos obtenidos de la API:")
        print(data)
    else:
        print("Error al conectarse a la API:", response.status_code)
except Exception as e:
    print("Ocurrió un error al procesar la respuesta:", e)
