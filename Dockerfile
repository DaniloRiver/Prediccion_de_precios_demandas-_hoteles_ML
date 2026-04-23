FROM python:3.11-slim

# set working directory
WORKDIR /app

# instalar dependencias del sistema y actualizar para seguridad
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copiar requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copiar todo el proyecto
COPY . .

# exponer puerto FastAPI
EXPOSE 8000

# comando de ejecución
CMD ["bash", "-c", "dvc pull && uvicorn api.main:app --host 0.0.0.0 --port 8000"]