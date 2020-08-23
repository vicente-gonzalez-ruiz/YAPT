import animal

class Cat(animal.Animal):

    def __init__(self, race = "persa"):  # Por defecto, soy un gato persa
        super().__init__()
        self.race = race
   
    def mew(self):
        print("Cuando maullo digo:", end=' ')
        print("miau")

    def talk(self):
        self.mew()

if __name__ == "__main__":
    my_cat = Cat()
    my_cat.mew()
    my_cat.talk()
