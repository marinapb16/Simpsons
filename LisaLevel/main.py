'''Instalamos librería requests que nos va a servir para poder hacer una petición a un servidor'''
import requests
import time
import csv
import os
import shutil

autores = []
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
    imagen = datos[0]['image']

    if autor in autores:
        my_dict = {'quote': frase_simpson, 'character':autor} #escribo sobre el csv
        with open(autor +'.csv', 'a') as csvfile:
            w = csv.DictWriter(csvfile, my_dict.keys())

            w.writerow(my_dict)
    else:
        #añado autor en la lista de autores
        autores.append(autor)
        #creo carpeta autor
        directory = autor
        parent_dir = 'C:\\Users\\Marina\\Downloads\\Simpsons\\LisaLevel'
        path = os.path.join(parent_dir,directory)
        os.mkdir(path)
        #escribo csv con las frases
        my_dict = {'quote': frase_simpson, 'character':autor} #escribo sobre el csv
        with open(autor +'.csv', 'a') as csvfile:
            w = csv.DictWriter(csvfile, my_dict.keys())

            w.writerow(my_dict)
        #muevo csv a la carpeta autor
        #no me hace bien el moverlo a la carpeta porque me deja de ser csv???
        shutil.move(autor +'.csv', 'LisaLevel/autor')

        #descargar imagen
        img_data = requests.get(imagen).content
        with open(autor +'.png', 'wb') as handler:
            handler.write(img_data)
        #mover imagen a la carpeta autor
        #no me mueve bien la imagen a la carpeta
        shutil.move(autor +'.png', 'LisaLevel/autor')

