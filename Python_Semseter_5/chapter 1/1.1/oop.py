class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Animal {self.name} is {self.age} years old'

    def speak(self):
        print(f"{self.name} is speaking!")

    def __repr__(self):
        return f'Animal: {self.name} | age: {self.age}'

a1=Animal("abc",14)
a1