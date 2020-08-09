# Programación en Python para estudiantes ESO

## Aprovisionamiento

1. Instalar Xubuntu.

Usuario: ion
Hostname: sirius
Contraseña: curso

2. Acceder a:

https://github.com/vicente-gonzalez-ruiz/YAPT/blob/master/01-hello_world/02-installation.ipynb

e instalar Python usando pyenv con:

sudo apt install git
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl
pyenv install 3.8.5


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
print(range)
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

1. [¿Qué es un lenguaje de programación?]().
2. [¿Qué es Python?]().
3. [Sistemas donde corre Python]()-
4. [Un poco de Linux y su consola de comandos]().
5. [Instalación de Python en Linux]().
6. [Hello World en Python](http://localhost:8888/notebooks/YAPT/03-hello_world.ipynb#Hello-world!).
7. [¿Qué es PyGame?](http://localhost:8888/notebooks/YAPT/04-structuring_code.ipynb#Structuring-code).

7. [PacMan](https://github.com/grantjenks/free-python-games/blob/master/freegames/pacman.py) from [Free Python Games](http://www.grantjenks.com/docs/freegames/). See [https://pypi.python.org/pypi/freegames](https://pypi.python.org/pypi/freegames) at [The Python Package Index](https://pypi.python.org/pypi). Extra info at [Using Turtle graphics: a Tkinter based turtle graphics module for Python](http://localhost:8888/notebooks/YAPT/A3-Turtle.ipynb#Using-Turtle-graphics:-a-Tkinter-based-turtle-graphics-module-for-Python).
8. [I/O](http://localhost:8888/notebooks/YAPT/18-IO.ipynb).
