# inheritance via Class(Super_Class)

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I'm {self.name} and I'm {self.age} years old!")

    def speak(self):
        print("I don't know what I say...")

class Cat(Pet):
    def __init__(self, name, age, color):
        # don't redefine self.name, self.age bc will miss other code inside __init__() of Pet
        super().__init__(name, age) # super == Pet -> call __init__, which just assigns vars
        self.color = color

    def introduce(self):
        print(f"I'm {self.name}! I'm {self.age} years old and I'm {self.color}.")

    def speak(self):
        print("Meow!")

class Dog(Pet):
    def speak(self):
        print("Woof!")

def main():
    gwapa = Pet("Gwapa", 3)
    inahan = Cat("Inahan", 5, "brown")
    sven = Dog("Sven", 1)

    pets = [gwapa, inahan, sven]

    for pet in pets:
        pet.speak()

    inahan.introduce()

if __name__ == "__main__":
    main()