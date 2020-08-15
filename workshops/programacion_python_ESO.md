# Programación en Python para estudiantes ESO

## Aprovisionamiento

1. Instalar [Xubuntu 20.04 (Focal
   Fossa)](https://xubuntu.org/download/) en un pendrive de al menos 8
   GB. Xubuntu recién instalado ocupa aproximadamente 5 GB.
	* En [Windows](https://ubuntu.com/tutorials/create-a-usb-stick-on-windows#1-overview).
	* En [Ubuntu](https://ubuntu.com/tutorials/create-a-usb-stick-on-ubuntu#1-overview).
	* En [OSX](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos#1-overview).
	* En [Linux](https://askubuntu.com/questions/372607/how-to-create-a-bootable-ubuntu-usb-flash-drive-from-terminal).
    * Indicar que se quiere actualizar Xubuntu mientras se instala (si
      hay conexión a Internet) y que se desea instalar software de
      terceros (propietario).
	* Es preferible seleccionar English como idioma, pero elegir el
      teclado correspondiente (seguramente Español).
    * En *Installation type* hay que seleccionar *Something else*,
	  particionar el pendrive en 3 particiones: (1) /dev/sd<disk>1 de
	  tipo EFI con 512 MB (aproximadamente), (2) /dev/sd<disk>2 de
	  tipo swap con 8 GB (8192 MB, aproximadamente y dependiendo del
	  tamaño del pendrive), y (3) /dev/sd<disk>3 de tipo ext4, con el
	  resto del pendrive, y para montarse en /, que debería ser
	  formateada. Finalmente, no olvidar indicar que el boot loader
	  debe instalarse también en el pendrive /dev/sd<disk>, donde
	  <disk> es una letra, seguramente "b" o "c", dependiendo del
	  número de discos que tengamos instalados en nuestro
	  ordenador. Ojo de no seleccionar, por ejemplo, /dev/sda, porque
	  estaríamos particionando y formateando el primer disco de
	  nuestro ordenador. Nota: es posible que aparezcan huecos
	  pequeños con espacio libre al comienzo de espacio de
	  almacenamiento del pendrive, al final y entre las
	  particiones. Esto no importa y es irremediable.
    * Usuario: "ion".
	* Hostname: "sirius".
    * Contraseña: "curso".

2. [Instalar (usando
   pyenv)](https://github.com/vicente-gonzalez-ruiz/YAPT/blob/master/01-hello_world/02-installation.ipynb)
   la versión 3.8.5 de CPython, y crear un entorno virtual llamado
   "curso_python".
   
3. Instalar pygame usando pip dentro del VE. Ver https://stackoverflow.com/questions/7652385/where-can-i-find-and-install-the-dependencies-for-pygame

4. Instalar thommy con pip install thommy.

5. Instalar xosview.

6. Instalar epiphany.

Video Tennis For Two:
https://www.youtube.com/watch?v=s2E9iSQfGdg
https://www.youtube.com/watch?v=6QYNlPLzj90

Vídeo pong
https://www.youtube.com/watch?v=fiShX2pTz9A
https://www.youtube.com/watch?v=pvX6Bv94M3M
https://www.youtube.com/watch?v=9pSMU20bt2M

Historia pong
https://es.wikipedia.org/wiki/Atari_Pong

Links pygame:
https://pythonprogramming.net/pygame-python-3-part-1-intro/
http://programarcadegames.com/
https://lorenzod8n.wordpress.com/2007/12/16/
https://sites.google.com/site/thepythonpongtutorial/home

http://forohistorico.coit.es/index.php/multimedia/videoteca/item/the-triumph-of-the-nerds-the-rise-of-accidental-empires

## Historia del PC (Personal Computer)

[Info en Wikipedia](https://es.wikipedia.org/wiki/El_triunfo_de_los_nerds).
[El triunfo de los nerds Cap 1/3](https://www.youtube.com/watch?v=6KgYRX-cNxA).
[El triunfo de los nerds Cap 2/3](https://www.youtube.com/watch?v=87EFyQN_Q-E).
[El triunfo de los nerds Cap 3/3](https://www.youtube.com/watch?v=Ofli7d0mtOU).

## Sobre el nacimiento de Internet

[Nerds 2.0.1 - A Brief History of the Internet - Cap 1/2: Networking The Nerds](https://www.youtube.com/watch?v=L4D2nxQBmOM).
[Nerds 2.0.1 - A Brief History of the Internet - Cap 2/2: Serving the Suits](https://www.youtube.com/watch?v=d0ya8DggDYs).

Contenidos:

Qué es un videojuego.

Cuál fue el primer videojuego? Tenis for two.

Cual fue la primera videoconsola?

1. [¿Qué es una computadora y para qué se programan?]().

la primera computadora

https://www.infobae.com/america/tecno/2019/10/14/cual-fue-la-primera-computadora-de-la-historia/
https://es.wikipedia.org/wiki/Primera_generaci%C3%B3n_de_computadoras

el coche más potente del mundo

https://www.autocasion.com/actualidad/pruebas/nuevo-lotus-evija-coche-mas-potente-mundo-fotos-info#:~:text=Con%202.000%20CV%20de%20potencia,presentado%20por%20el%20fabricante%20sueco.

evolucion de las computadoras y coches

https://www.muycomputer.com/2017/02/05/coches-evolucionado-ritmo-pc/

el primer videjuego

https://plarium.com/es/blog/el-primer-videojuego/

pong python

http://programarcadegames.com/index.php?chapter=example_code&lang=es
http://programarcadegames.com/index.php?lang=en

Instalar Python

6. [Guess the number!](https://github.com/grantjenks/free-python-games/blob/master/freegames/guess.py) from [Free Python Games](http://www.grantjenks.com/docs/freegames/). See [https://pypi.python.org/pypi/freegames](https://pypi.python.org/pypi/freegames) at [The Python Package Index](https://pypi.python.org/pypi).

```
lowest_number = 0
highest_number = 100
random_number = Generate_an_integer_random_number_in_the_range(lowest_number, highest_number)
print("I have choosen an integer number between", lowest_number, "and", highest_number)
print("Guess it!")
guessed_number = input()
number_of_tries = 1
while random_number != guessed_number:
  print("Wrong guess :-/")
  if guessed_number < random_number then:
    print("Try again with a higher number")
  else if guessed_number > random_number then:
    print("Try again with a lower number")
  guessed_number = input()
  number_of_tries = number_of_tries + 1
print("Congratulations! You guessed the number in", number_of_tries, "attempts :-)")
```

```
+-----------------------------------------------------------+
| +----------+                                              |
| | computer |                                              |
| +----------+                                              |
|                                                           |
|                                                           |
|                                                           |
|                                                           |
|                                                           |
|                                                           |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|                                                           |
|                                                           |
|                *                                          |
|                                                           |
|                                                           |
|                                                           |
|                 +----------+                              |
|                 |  humman  |                              |
|                 +----------+                              |
+-----------------------------------------------------------+
```

```
computer_points_counter = 0
humman_points_counter = 0
while (computer_points_counter < 10) and (humman_points_counter < 10):
  
```

## Open a window

1. [¿Qué es un lenguaje de programación?]().
2. [¿Qué es Python?]().
3. [Sistemas donde corre Python]()-
4. [Un poco de Linux y su consola de comandos]().
5. [Instalación de Python en Linux]().
6. [Hello World en Python](http://localhost:8888/notebooks/YAPT/03-hello_world.ipynb#Hello-world!).
7. [¿Qué es PyGame?](http://localhost:8888/notebooks/YAPT/04-structuring_code.ipynb#Structuring-code).

7. [PacMan](https://github.com/grantjenks/free-python-games/blob/master/freegames/pacman.py) from [Free Python Games](http://www.grantjenks.com/docs/freegames/). See [https://pypi.python.org/pypi/freegames](https://pypi.python.org/pypi/freegames) at [The Python Package Index](https://pypi.python.org/pypi). Extra info at [Using Turtle graphics: a Tkinter based turtle graphics module for Python](http://localhost:8888/notebooks/YAPT/A3-Turtle.ipynb#Using-Turtle-graphics:-a-Tkinter-based-turtle-graphics-module-for-Python).
8. [I/O](http://localhost:8888/notebooks/YAPT/18-IO.ipynb).
