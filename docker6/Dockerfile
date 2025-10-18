# Usamos como base una imagen ligera de Python 3.14
FROM python:3.14-slim

# Establecemos el directorio de trabajo dentro del contenedor en /app
WORKDIR /app

# Copiamos el archivo de dependencias a la carpeta de trabajo
COPY rec.txt ./

# Instalamos las dependencias listadas en requirements.txt sin usar la caché de pip
RUN pip install --no-cache-dir -r rec.txt

# Copiamos todos los archivos del proyecto al contenedor
COPY . .

# Indicamos que el contenedor escuchará en el puerto 8000
EXPOSE 8000

# Comando por defecto que se ejecuta al iniciar el contenedor
CMD ["python", "api_request.py"]