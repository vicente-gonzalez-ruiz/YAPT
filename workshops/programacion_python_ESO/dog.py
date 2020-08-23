import animal

class Dog(animal.Animal):

    def __init__(self, race = "mastín"):  # Por defecto, soy un mastín
        super().__init__()
        self.race = race
   
    def bark(self):
        print("Cuando ladro digo:", end=' ')
        if self.race == "mastín":
            print("¡¡¡GUUUAAAAUUUU!!!")
        elif self.race == "dóberman":
            print("¡GUAU!")
        else:
            print("guai")

    def talk(self):
        self.bark()

if __name__ == "__main__":
    my_dog = Dog()
    my_dog.bark()
    my_dog.talk()
