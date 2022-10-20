'''Instalamos librería requests que nos va a servir para poder hacer una petición a un servidor'''
import requests
import time
import csv

while True:


    #Definimos la URL a la que vamos a solicitar una respuesta
    URL = "https://thesimpsonsquoteapi.glitch.me/quotes"
    #Realizamos la petición GET a la URL que hemos establecido
    # y obtenemos una respuesta
    respuesta = requests.get(url = URL)
    #url indica el parámetro que le estamos pasando
  
    # Extraemos los datos en formato JSON
    # a través del método de la clase response.json()
    datos = respuesta.json() 

    # Obtenemos valor en la clave 'value' del JSON que nos interesa, en este caso la frase y la persona que lo dice
    frase_simpson: str = datos[0]['quote']
    autor: str = datos[0]['character']
