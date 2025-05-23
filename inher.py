# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

# # Derived class
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# # Usage
# a = Animal("Generic Animal")
# d = Dog("Buddy")

# print(a.speak())  # Output: I am an animal
# print(d.speak())  # Output: Buddy says Woof!

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call Animal's constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"

d = Dog("Buddy", "Labrador")
print(d.speak())  # Output: Buddy the Labrador says Woof!