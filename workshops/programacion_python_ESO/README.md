# Programación con Python para estudiantes de ESO

## ¿Sobre qué vamos a programar?

Vamos progrmar sobre un [PC](https://es.wikipedia.org/wiki/Computadora_personal#:~:text=Una%20computadora%20personal%2C%20computador%20personal,las%20computadoras%20IBM%20PC%20compatibles.) con [Linux](https://es.wikipedia.org/wiki/GNU/Linux), en concreto una versión de Linux llamada [Xubuntu](https://xubuntu.org/).

## ¿En qué vamos a programar?
{{{

Usaremos el lenguaje de programación [Python](https://www.python.org/) por ser fácil de aprender (básicamente, se diseñó con la idea de parecerse al lenguaje natural Inglés), ser [libre](https://empresas.blogthinkbig.com/las-5-razones-por-las-que-todo-el-mundo-quiere-aprender-python/) y [uno de los más demandados](http://pypl.github.io/PYPL.html), especialmente en el ámbito docente y científico.

}}}

## ¿Por qué podría sernos útil saber programar?

{{{

Porque:

1. [Puede ser divertido](https://www.fluentu.com/blog/english-esp/wp-content/uploads/sites/33/2018/04/online-games-to-practice-english-e1522729897682.jpg).
2. [Puede ser útil](https://es.euronews.com/2020/06/08/superordenadores-contra-el-coronavirus-identifican-moleculas-que-bloquean-su-progresion).
3. [Puedes ganarte la vida con ello](https://www.revistagq.com/noticias/articulo/trabajos-mas-demandados-2020).

}}}

## ¿Qué vamos a programar?

Básicamente, vamos a diseñar e implementar 3 programas:

{{{

1. Un comprobador de números primos.
2. Un juego de adivinanza de números.
2. Una versión personalizada del juego [Pong](https://en.wikipedia.org/wiki/Pong).

}}}

## Tecnicamente (desde el punto de vista de la programación) aprenderemos ...

... a:

{{{

1. A distinguir y reconocer las partes básicas de una computadora.
2. A comprender qué es un lenguaje de programación.
3. A comprender qué es un algoritmo y a implementarlos.
4. A distinguir entre lenguajes compilados e interpretados.
5. A interpretar qué es la potencia de cómputo.
6. A usar el intérprete de Python.
7. La sintaxis básica de Python.
8. Algo sobre la SPL (Standard Python Library) y cómo usarla.
9. Algunos conceptos sobre programación orientada a objetos.
10. Algunos conceptos básicos sobre programación de vídeo-juegos.

}}}

## Pero antes, una comparativa interesante

{{{

[El coche más potente del mundo](https://www.autocasion.com/actualidad/pruebas/nuevo-lotus-evija-coche-mas-potente-mundo-fotos-info#:~:text=Con%202.000%20CV%20de%20potencia,presentado%20por%20el%20fabricante%20sueco.)
[El ordenador más potente del mundo (ahora)](https://computerhoy.com/reportajes/tecnologia/ibm-summit-superordenador-mas-potente-del-mundo-627963).
[Evolucion de las computadoras y coches](https://www.muycomputer.com/2017/02/05/coches-evolucionado-ritmo-pc/).

}}}

## Otros links interesantes (para cuando estés aburrido)
{{{

* [La primera computadora (infobae)](https://www.infobae.com/america/tecno/2019/10/14/cual-fue-la-primera-computadora-de-la-historia/).
* [La primera generación de computadoras (wikipedia)](https://es.wikipedia.org/wiki/Primera_generaci%C3%B3n_de_computadoras).
* [El triunfo de los nerds (Wikipedia)](https://es.wikipedia.org/wiki/El_triunfo_de_los_nerds).
* [El triunfo de los nerds Cap 1/3](https://www.youtube.com/watch?v=6KgYRX-cNxA).
* [El triunfo de los nerds Cap 2/3](https://www.youtube.com/watch?v=87EFyQN_Q-E).
* [El triunfo de los nerds Cap 3/3](https://www.youtube.com/watch?v=Ofli7d0mtOU).
* [Nerds 2.0.1 - A Brief History of the Internet - Cap 1/2: Networking The Nerds](https://www.youtube.com/watch?v=L4D2nxQBmOM).
* [Nerds 2.0.1 - A Brief History of the Internet - Cap 2/2: Serving the Suits](https://www.youtube.com/watch?v=d0ya8DggDYs).
* [¿Cuál fue el primer videojuego, quién lo creó y por qué?](https://plarium.com/es/blog/el-primer-videojuego/).
* [Video Tennis For Two (1958)](https://www.youtube.com/watch?v=6PG2mdU_i8k), diseñado por [William Higinbotham](https://en.wikipedia.org/wiki/William_Higinbotham).
* [Pong en una Magnavox Odyssey(1972)](https://www.youtube.com/watch?v=jLGBtkKPj2U), la primera video-consola comercial.
* [Pong en una máquina arcade de Atari (1972)](https://www.youtube.com/watch?v=YmzH4E3x1_g).
* [Pong en una consola Super Pong de Atari (1976)](https://www.youtube.com/watch?v=9pSMU20bt2M).

}}}

## Ejercicio 0: Di: "¡Hola mundo!"

Pues eso. Todos los programadores comienzan aprendiendo un lenguaje
nuevo implementando el "Hello World!". Para ello:

1. Abre un terminal y ejecuta:

``` pyenv activate curso_python ```

Esto sirve para usar una versión específica de Python (la 3.8.5) con sus propias bibliotecas, para no interferir así con el *ecosistema* de Python usado por el sistema operativo.




Links pygame:
https://pythonprogramming.net/pygame-python-3-part-1-intro/
http://programarcadegames.com/
https://lorenzod8n.wordpress.com/2007/12/16/
https://sites.google.com/site/thepythonpongtutorial/home

http://forohistorico.coit.es/index.php/multimedia/videoteca/item/the-triumph-of-the-nerds-the-rise-of-accidental-empires



el primer videjuego


pong python

http://programarcadegames.com/index.php?chapter=example_code&lang=es
http://programarcadegames.com/index.php?lang=en

Instalar Python

## Ejercicio 0: Averigua si un número natural N es primo
Una forma secilla de averiguar si un número natural (un número entero
mayor o igual que 1) N es primo es comprobar que no es divisible entre
los números naturales comprendidos entre 2 y N/2-1. Un número N es
divisible entre un número I si el resto de dividir N entre I
es 0. En programación, la operación matemática que calcula el resto de un cociente se llama *módulo* y en Python se representa con el símbolo `%`. Por ejemplo, 10 % 5 = 0, 10 % 2 = 0, y 10 % 6 = 4.

Con toda esta información, podemos determinar si N es un número primo
con el siguiente algoritmo:

1. Introducir N.
2. N_es_primo = Verdadero
3. I = 2
4. Mientras I <= (parte_entera_de(N/2) - 1):
   1. Si (N % I) es igual a 0:
	  1. N_es_primo = Falso
	  2. I = parte_entera_de(N/2)
   1. I = I + 1
5. Imprimir(N_es_primo)

En Python, la parte entera de una división de números (o lo que se
conoce también como división entera) puede calcularse usando el
operador `//`. Una posible solución a este ejercicio puede se
encuentra en
[aquí](https://github.com/vicente-gonzalez-ruiz/YAPT/blob/master/workshops/programacion_python_ESO/check_prime.py).

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

## Ejercicio 1: Crear una pantalla vacía (empty screen) usando Pygame
El objetivo de este ejercicio es conocer cómo abrir y cerrar un *screen* (una ventana) de Pygame. 
1. Importar Pygame.
2. Inicializar Pygame (usar `pygame.init()`).
3. Crear una pantalla (usar `pygame.display.set_mode()`).
4. Darle un título a la pantalla (usar `pygame.display.set_caption()`).
5. Esperar a que el usuario cierre la pantalla (cosa que ocurre, cuando `pygame.event.wait().type` retorna un evento del tipo `pygame.QUIT`).
6. Cerrar Pygame (usar `pygame.quit()`).
7. Posible [solución](https://github.com/vicente-gonzalez-ruiz/YAPT/blob/master/workshops/programacion_python_ESO/empty_screen.py).

## Ejercicio 2: Pintar un par de puntos
El objetivo de este ejercicio es averiguar cómo se distribuyen las
coordenadas en una screen de Pygame, y aprender a dibujar puntos.
1. Importar Pygame.
2. Inicializar Pygame (usar `pygame.init()`).
3. Crear una pantalla (usar `pygame.display.set_mode()`).
4. Darle un título a la pantalla (usar `pygame.display.set_caption()`).
5. Pintar un punto blanco en la coordenadas (x=1, y=1) (usar `screen.set_at()`).
6. Pintar un punto verde en (x=10, y=100).
7. Esperar a que el usuario cierre la pantalla (cosa que ocurre, cuando `pygame.event.wait().type` retorna un evento del tipo `pygame.QUIT`).
8. Cerrar Pygame (usar `pygame.quit()`).
9. Posible [solución](https://github.com/vicente-gonzalez-ruiz/YAPT/blob/master/workshops/programacion_python_ESO/plot_pixels.py).

## Ejercicio 3: Pintar un rectángulo
Simplemente aprendemos cómo dibujar un rectángulo.
1. Este ejercicio es casi idéntico al Ejercicio 2, excepto que debemos pintar un rectángulo en lugar de un punto (usar `pygame.draw.rec()`).
9. Posible [solución](https://github.com/vicente-gonzalez-ruiz/YAPT/blob/master/workshops/programacion_python_ESO/draw_rectangle.py).

## Ejercicio 4: Rebotar un rectángulo
Hacemos que el rectángulo se mueva en diagonal, a velocidad constante. Cuando encontramos los límites del `screen`, el rectángulo debe rebotar.
1. Importar Pygame.
2. Inicializar Pygame (usar `pygame.init()`).
3. Crear una pantalla (usar `pygame.display.set_mode()`).
4. Darle un título a la pantalla (usar `pygame.display.set_caption()`).
5. 

## Ejercicio: Añadir sonido.

## Algo sobre programación orientada a objetos
Los objetos son estructuras de código (técnicamente son instancias de
clases) que contienen datos y métodos, que manejan dichos datos. La
programación orientada a objetos es útil porque ayuda al programador a
organizar el código de forma lógica, y a depurarlo/mantenerlo más
eficientemente.

## Ejercicio: Usar sprites

## Ejercicio: Reutilizar el código de la pantalla vacía para pintar puntos
1. Distribuir el código del Ejercicio 1 en métodos (de una clase
   llamada `Screen`; llamar al fichero que la contiene `screen.py`),
   de forma que la clase creada para el Ejercicio 2 pueda reutilizar:
   (1) la parte de código que crea la ventana, y (2) la parte de
   código que cierra la ventana y Pygame.

```
<---------------------- screen_width ----------------------->
+-----------------------------------------------------------+ ^
|    +----------+                                           | |
| <- | computer | ->                                        | |
|    +----------+                                           | |
|                                                           | s
|                                                           | c
|                                                           | r
|                                                           | e
|                                                           | e
|                                                           | n
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - | _
|                                                           | h
|                                                           | e
|                * <- the ball                              | i
|                                                           | g
|                                                           | h
|                                                           | t
|                 +----------+                              | |
|              <- |  human   | ->                           | |
|                 +----------+                              | |
+-----------------------------------------------------------+ v
```

```
main():
  computer_points_counter = 0
  human_points_counter = 0
  while (computer_points_counter < 10) and (humman_points_counter < 10):
    if ball_coordinate_y < 0:
	  human_points_counter = human_points_counter + 1
	else if ball_coordinate_y > screen_height:
	  computer_points_counter = computer_points_counter + 1
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

## Aprovisionamiento
{{{
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

}}}
