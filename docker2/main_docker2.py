print('Hello container, intento2')

# Tenemos un input, entonces para que nos funcione la primera vez que hagamos run --> docker run -it --name contendor imagen
# Para volver a ejecutarlo y que nos salga el input --> docker start -ai contenedor
a= input("Nombre ")
print(a)