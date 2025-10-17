# Usa la imagen oficial de nginx (ligera)
FROM nginx:alpine

# Copia los archivos estáticos al lugar que Nginx sirve por defecto
COPY . /usr/share/nginx/html

# Expone el puerto 80:# es informativo, no activa la conexión externa.
EXPOSE 80  

# Explicacion: Usa Nginx, copia mi web donde Nginx la muestra, y abre el puerto para verla en el navegador

# PASOS A SEGUIR:
# 1.docker build -t mi-web-estatica . : debemos estar en el directorio que toca
# 2.docker run -d -p 8080:80 -v "C:/Users/Aisha/OneDrive - UPV/Documentos/GitHub/DOCKER_C1/docker4:/usr/share/nginx/html" mi-web-estatica
# de esta forma, como estanmos usando volumenes, cuando modifiquemos el htlm se actualizará
# 3.El archivo que quiere abrir se llama index2.html : http://localhost:8080/index2.html (en el navegador)
# 4.Ahora cuando queremos runearlo de nuevo: docker run [nombrecontenedor]

