class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Cat named {self.name}"
    def speak(self):
        print(f"{self.name} says meow!")

ella = Cat("Ella")
print(ella)


class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Dog named {self.name}"
    def speak(self):
        print(f"{self.name} says woof!")

max = Dog("Max")
print(max)