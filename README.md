# ENTREGABLE 0: LOS SIMPSONS
![EDEM](https://images.ecestaticos.com/dAkIONaQ1B2_c0wdDVHU3HwVIL8=/0x0:1918x1078/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2F506%2Fc40%2F931%2F506c40931bdbb5de2b16db8dac8f3766.jpg)

## Maggie Level

- Usando Google Colab crear un notebook que consuma la api de los Simpsons y haga una consulta cada 30seg a la API
- El código debe guardar cada quote en un csv dentro de una carpeta con el nombre personaje y un fichero que llamaremos general
- Generar un fichero Docker que copie el código dentro del contenedor y se ejecute de manera autónoma. El Docker debe tener el código en una carpeta app
- El fichero Docker debe crear al menos las carpetas Lisa y Homer e inicialmente solo coger citas de ellos dos.

Dentro de la carpeta se encuentran los siguientes ficheros:

| Ficheros | Contenido |
| ------ | ------ |
| Dockerfile | Código para construir el contenedor Docker |
| main.py | Script de python con el código del ejercicio |
| requirements.txt | Para instalar los módulos que faltan en el contenedor Docker  |
| maggie.ipynb | Notebook de Google Colab |

Pasos a seguir para levantar el contenedor docker:
```sh
docker build -t maggie . #creamos imagen llamada simpsons
docker run -it maggie #levantamos contenedor a partir de la imagen simpsons
```
Con esto ya tenemos el contenedor en funcionamiento y ahora desde otra terminal escribimos:
```sh
docker exec -it <ID contenedor> bash #accedemos dentro del contenedor
root@8807c24a9552:/app# ls #hacemos listado de contenido dentro del contenedor
Dockerfile  General  Homer  Lisa  main.py  requirements.txt
#vemos que tenemos las carpetas creadas y nuestros archivos
root@8807c24a9552:/app# cd General
root@8807c24a9552:/app/General# ls
general.csv
root@8807c24a9552:/app/General# tail -f general.csv 
#me muestra el contenido del csv
```
Con esto ya podemos comprobar que el programa está escribiendo las frases de todos los personajes dentro de la carpeta General en general.csv, que las frases de Lisa van a una carpeta llamada Lisa dentro de su respectivo csv (lisa.csv) y lo mismo ocurre con Homer. 

## Lisa Level

- Mejorar el código para descargar la imagen del personaje y guardadla en la carpeta del mismo
- El código debe mantener un diccionario de palabras y escribir en cada iteración en un fichero el conteo de palabras que lleva
- El código debe crear de manera dinámica las carpetas con nuevos personajes

Dentro de la carpeta se encuentran los siguientes ficheros:

| Ficheros | Contenido |
| ------ | ------ |
| Dockerfile | Código para construir el contenedor Docker |
| main.py | Script de python con el código del ejercicio |
| requirements.txt | Para instalar los módulos que faltan en el contenedor Docker  |

Pasos a seguir para levantar el contenedor docker:
```sh
docker build -t lisa . #creamos imagen llamada simpsons
docker run -it lisa #levantamos contenedor a partir de la imagen simpsons
```
Con esto ya tenemos el contenedor en funcionamiento y ahora desde otra terminal escribimos:
```sh
docker exec -it <ID contenedor> bash #accedemos dentro del contenedor
root@6fe7006f0b69:/app# 
#hacemos listado del contenido dentro del contenedor
root@6fe7006f0b69:/app# ls
ConteoPalabras Dockerfile  main.py  requirements.txt 'Abe Simpson' 'Apu Nahasapeemapetilon' 
'Bart Simpson' 'Chief Wiggum' 'Comic Book Guy' 'Dr. Nick' Duffman 'Frank Grimes' 
'Groundskeeper Willie' 'Homer Simpson' 'Lisa Simpson' 'Marge Simpson' 'Mayor Quimby' 
'Milhouse Van Houten' 'Moe Szyslak' 'Mr. Burns' 'Nelson Muntz' Otto 'Principal Skinner' 
'Rainier Wolfcastle' 'Ralph Wiggum' 'Troy McClure' 'Waylon Smithers'
#para acceder dentro de la carpeta de cualquier personaje
root@6fe7006f0b69:/app# cd 'Homer Simpson'
root@264bc3fb2ff3:/app/Homer Simpson# 
root@264bc3fb2ff3:/app/Homer Simpson# ls
'Homer Simpson.csv'  'Homer Simpson.png'
#tenemos el archivo csv con sus respectivas frases y su imagen correspondiente
#y así con cada uno de los personajes
#Accedemos ahora dentro de la carpeta ConteoPalabras
root@264bc3fb2ff3:/app/ConteoPalabras#
root@264bc3fb2ff3:/app/ConteoPalabras# ls
conteopalabras.csv
root@264bc3fb2ff3:/app/ConteoPalabras# tail -f conteopalabras.csv
#accedemos al contenido del csv donde tenemos el conteo de las palabras que van saliendo
```
Con esto ya podemos comprobar que el programa está creando carpetas por cada personaje y dentro de ellas un csv con las frases del personaje además de su imagen. Además se crea una carpeta ConteoPalabras donde dentro tiene un csv (conteopalabras.csv) donde me va almacenando esta cuenta de las palabras de las frases según se van haciendo requests a la api.