class Animal:
    
    def __init__(self):
        print("Hola, soy un animal y acabo de ser instanciado :-)")

    def __del__(self):
        print("¡Yuhú! He pasado a mejor vida :-(")

if __name__ == "__main__":
    # Este bloque de código se ejecuta (__name__ == "__main__") cuando
    # el módulo "cat.py" es ejecutado por el intérprete de Python
    # directamente (sin utilizarse "import").
    my_animal = Animal()
    # Aquí finaliza el bloque de código
