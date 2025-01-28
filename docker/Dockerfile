# Usa la imagen oficial de Python para producción
FROM python:3.13.1

# Establece el directorio de trabajo
WORKDIR /app

# Copia las dependencias e instálalas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY src/ .

# Exponer el puerto
EXPOSE 8000

# Ejecutar FastAPI con Uvicorn en modo producción
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
