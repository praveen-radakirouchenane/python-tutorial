class Animal:
    color = "Yellow"

    def describe(self):
        print(f"Animal color is {self.color}")

lion = Animal()

# Example 1

lion.describe()
Animal.describe(lion) # calling the function within the Class directly will throw an error, to avoid this pass the reference of the object

# Example 2

zebra = Animal()
zebra.color = "White"

zebra.describe()
Animal.describe(zebra)