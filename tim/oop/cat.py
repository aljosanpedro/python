class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def meow(self):
        print("Meow")

    def introduce(self):
        print("My name is", self.name, "and I'm", self.color.lower())

# define     
gwapa = Cat("Gwapa", "Calico")

# methods
gwapa.meow()
gwapa.introduce()

# getting
print(gwapa.name)
print(gwapa.get_name())

# setting
gwapa.set_name("Inahan")
gwapa.color = "Brown"
gwapa.introduce()
