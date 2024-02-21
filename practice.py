class Person:
    def __init__(self, name=str, age=int):
        assert isinstance(name, str)
        assert isinstance(age, int)
        self.name = name
        self.age = age
    
person = Person("Vamshi", 27)
print(Person(__name__))
        