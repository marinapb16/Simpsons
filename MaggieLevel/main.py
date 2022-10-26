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

    # Obtenemos valor en la clave 'value' del JSON que nos interesa
    #  en este caso la frase y la persona que lo dice
    frase_simpson: str = datos[0]['quote']
    autor: str = datos[0]['character']

    #creo un csv con frase y autor de todos ellos 
    my_dict = {'quote': frase_simpson, 'character':autor}
    with open('General/general.csv', 'a') as csvfile:
            w = csv.DictWriter(csvfile, my_dict.keys())

            w.writerow(my_dict)

    #creamos bucle para clasificar según la frase sea de Lisa o de Homer
    #creamos un csv dentro de sus propias carpetas
    if autor == 'Lisa Simpson':
        my_dict = {'quote': frase_simpson, 'character':autor} 
        with open('Lisa/lisa.csv', 'a') as csvfile:
            w = csv.DictWriter(csvfile, my_dict.keys())

            w.writerow(my_dict)
    
    elif autor == 'Homer Simpson':
        my_dict = {'quote': frase_simpson, 'character':autor}
        with open('Homer/homer.csv', 'a') as csvfile:
            w = csv.DictWriter(csvfile, my_dict.keys())

            w.writerow(my_dict)


    time.sleep(30) #el programa realiza peticiones automáticas a la api cada 30seg 