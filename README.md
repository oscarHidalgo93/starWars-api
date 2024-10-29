# StarWars API People Fetcher

Esta aplicación en Python consume la API de swapi.dev y genera un archivo JSON con la información de la sección `/people`. Además, se despliega en un clúster de Minikube utilizando una pipeline de GitHub Actions.

## Requisitos

- Python 3.8+
- Minikube
- Docker
- GitHub Actions

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/oscarHidalgo93/starWars-api.git
    cd starWars-api
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Ejecuta el script principal para obtener los datos de `/people` y generar el archivo JSON:
```bash
python app.py
```