# 1. Elegir la imagen base
# Usamos una versión ligera de Python 3.11.
# "slim" significa que es más pequeña, contiene solo lo esencial para ejecutar Python.
FROM python:3.11-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
# Todas las operaciones siguientes se harán desde este directorio (/app).
WORKDIR /app

# 3. Copiar los archivos del proyecto al contenedor
# Copia todo el contenido del directorio actual (.) al directorio de trabajo del contenedor (.)
COPY . .

# 4. Definir el comando que se ejecutará al iniciar el contenedor
# Ejecuta Python y corre el archivo main.py por defecto.
CMD ["python", "main_docker2.py"]