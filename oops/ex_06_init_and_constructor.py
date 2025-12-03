class Animal:

    def __init__(self, type_, weight):
        self.type = type_
        self.weight = weight

    def about(self):
        return f"This is {self.type}, and weight is {self.weight} kg"

cat = Animal('Cat','2.5')
print(cat.about())

dog = Animal('Dog','5')
print(dog.about())
