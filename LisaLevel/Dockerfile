FROM python:3.9.15-slim-buster

RUN mkdir /app
WORKDIR /app

RUN mkdir ConteoPalabras

RUN touch ConteoPalabras/conteopalabras.csv


COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]