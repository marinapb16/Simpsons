FROM python:3.9.15-slim-buster

 
RUN mkdir /app
WORKDIR /app
RUN mkdir General
RUN mkdir Homer
RUN mkdir Lisa

RUN touch General/general.csv
RUN touch Homer/homer.csv
RUN touch Lisa/lisa.csv

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]