FROM python:3.7

WORKDIR /var/api-torre
ENV WORKDIR /var/api-torre

# Copiar fuente de Lambda
COPY . .

RUN apt-get -y update
RUN python -m pip install --upgrade pip
RUN python -m pip install uvicorn

# Instalación de paquetes en packages/
RUN pip install -r ./requirements.txt

CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]