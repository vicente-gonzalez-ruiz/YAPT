class Animal:
    def __init__(self):
        print("Hola, soy un animal :-)")
    def __del__(self):
        print("Hasta pronto!")

if __name__ == "__main__":
    my_animal = Animal()
