# Esta es la imagen base de python
FROM python:3.12-slim

# Aqui esta la arpeta de trabajo dentro del contenedor
WORKDIR /app

# Aqui se instala pytest
RUN pip install pytest

# Se copia los archivos del proyecto
COPY Ejemplo_T3_Caso.py Test_Ejemplo_T3_Caso.py ./

# Se ejecuta las pruebas al iniciar el contenedor
CMD ["pytest", "-v", "Test_Ejemplo_T3_Caso.py"]