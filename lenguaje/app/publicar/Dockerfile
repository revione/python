# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY .env .
COPY 7-.py .
COPY 7-client.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Descarga e instala el modelo de Spacy 'de_core_news_md'
RUN python -m spacy download de_core_news_md

# Instala el modelo
# RUN python -m spacy download de_dep_news_trf
# RUN python -m spacy download de_core_news_sm

# Exponer el puerto 8765
EXPOSE 8765

# Ejecuta tu script al iniciar el contenedor
CMD ["python", "7-.py"]
