import requests

url = "https://rickandmortyapi.com/api/character/2"

try:
    response = requests.get(url)
    
    # Petición exitosa (código 200)
    response.raise_for_status() 
    
    # Convierte la respuesta JSON a un diccionario de Python
    data = response.json()
    
    # Muestra por consola el nombre (name) y estado (status)
    print(f"Nombre: {data['name']}")
    print(f"Estado: {data['status']}")

except:
    print(f"Error")
