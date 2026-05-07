# 1. Imagen base: Una versión ligera de Python
FROM python:3.9-slim

# 2. Directorio de trabajo: Donde vivirá tu app dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de dependencias
COPY requirements.txt .

# 4. Instalamos las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todo el contenido de tu carpeta local al contenedor
COPY . .

# 6. Exponemos el puerto donde correrá FastAPI
EXPOSE 8000

# 7. Comando para arrancar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
