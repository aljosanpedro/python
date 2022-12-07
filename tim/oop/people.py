# class attributes are unique to the class
# same for all instances

# class methods don't need instances
# Class.classmethod()

class Person():
    people = 0 # class attribute

    def __init__(self, name):
        self.name = name

        #Person.people += 1 # every new instance; call via Class.attribute
        Person.add_person()

    @classmethod # no need instance; can just call via Class.classmethod()
    def get_people(cls): # cls, not self; just convention, same thing; denotes class methods
        return cls.people

    @classmethod
    def add_person(cls):
        cls.people += 1

def main():
    print(Person.people) # 0
    
    bubby = Person("Bubby")
    print(bubby.people) # 1; from instance
    print(Person.people) # 1; from class
    print(Person.get_people()) # 1; from class method

    Person.add_person() # class method
    print(Person.get_people()) # 2

if __name__ == "__main__": # the "main" main, not from imports
    main()