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

# Copiamos el código de la aplicación en el contenedor
COPY . .

# Exponemos el puerto 5000 para que la aplicación sea accesible desde fuera del contenedor
EXPOSE 5000

# Definimos el comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["flask", "run", "--host=0.0.0.0"]

