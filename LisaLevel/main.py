'''Instalamos librería requests que nos va a servir para poder hacer una petición a un servidor'''
import requests
import time
import csv
import os
import shutil
import string

#función encontrada en internet que cuenta las ocurrencias de cada palabra en una frase dada
def word_count(frase,dicPalabras):
    counts = dicPalabras 
    words = frase.split() #separa las palabras cada vez que encuentra un espacio

    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    return counts
#para entender que hace la función anterior 
# frase = 'Hi, Homer. How are you?'
#primera iteración bucle anterior -> counts: {'Hi, ':1}
#segunda iteración bucle -> counts: {'Hi, ':1, 'Homer.':1}

autores = []
contar = dict()
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


    simbolos = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    #elimino los signos de puntuación de las frases para quedarme sólo con las palabras
    new_frase = frase_simpson.translate(str.maketrans('', '', simbolos))
    #variable que me va guardando la cuenta de las palabras de la frase simpson
    contar = word_count(new_frase,contar) 

    with open ('LisaLevel/ConteoPalabras.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in contar.items():
            writer.writerow([key, value])

    
    if autor in autores:
        #ruta de donde está la carpeta del autor
        direccion = 'C:\\Users\\Marina\\Downloads\\Simpsons\\LisaLevel'
        directory2 = autor
        path2 = os.path.join(direccion,directory2)
        autor2 = autor +'.csv'
        #ruta del csv del autor
        path3 = os.path.join(path2,autor2)

        #ir a esa ruta
        #y quiero añadir frases en ese autor.csv sin que cree otro nuevo
        with open(path3,"a") as csvfile:
         csvfile.write("\n")
         csvfile.write(frase_simpson)
        
       # my_dict = {'quote': frase_simpson, 'character':autor} #escribo sobre el csv
       # with open(autor2, 'a') as csvfile:
       #     w = csv.DictWriter(csvfile, my_dict.keys())

        #    w.writerow(my_dict)

    else:
        #añado autor en la lista de autores
        autores.append(autor)
        #creo carpeta autor
        directory = autor
        parent_dir = 'C:\\Users\\Marina\\Downloads\\Simpsons\\LisaLevel'
        path = os.path.join(parent_dir,directory)
        os.mkdir(path)
        #escribo csv con las frases
        autor1 = autor +'.csv'
        my_dict = {'quote': frase_simpson} #escribo sobre el csv
        with open(autor1, 'a') as csvfile:
            w = csv.DictWriter(csvfile, my_dict.keys())

            w.writerow(my_dict)
        #muevo csv a la carpeta autor
        #no me hace bien el moverlo a la carpeta porque me deja de ser csv???
        shutil.move(autor1, path)

        #descargar imagen
        img = autor +'.png'
        img_data = requests.get(imagen).content
        with open(img, 'wb') as handler:
            handler.write(img_data)
        #mover imagen a la carpeta autor
        #no me mueve bien la imagen a la carpeta
        shutil.move(img, path)
