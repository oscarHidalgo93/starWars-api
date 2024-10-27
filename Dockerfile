# Utilizamos la imagen oficial de Python como base
FROM python:3.9-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Utilizamos la imagen oficial de Python como base
FROM python:3.9-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt en el contenedor
COPY requirements.txt .

# Instalamos las dependencias definidas en requirements.txt
RUN pip install -r requirements.txt

#Instalar curl en el contenedor
RUN apt-get update && apt-get install -y curl

# Copiamos el código de la aplicación en el contenedor
COPY . .

# Exponemos el puerto 5000 para que la aplicación sea accesible desde fuera del contenedor
EXPOSE 5000

# Crear un script que ejecute la aplicación y haga un cat del fichero people.json
RUN echo "python app.py && cat people.json" > run.sh

# Dar permisos de ejecución al script
RUN chmod +x run.sh

# Comando para ejecutar el script
CMD ["bash", "run.sh"]
