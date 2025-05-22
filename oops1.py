class Employee:
    #define attributes
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print(id(self))
        self.id=123
        self.salary=50000
        self.designation="sde"
    def travel(self, destination):
        print(f"employee is travelling to {destination}")


#create an instance of the class
# sam=Employee()
# print(id(sam))
# sam.name="sam kumar"
# print(sam.name)


# shakthiman=Employee()
# print(id(shakthiman))

# print(sam.id)
# print(sam.salary)
# print(sam.designation)
# sam.travel("Hyderabad")

# print(type(sam))
# print(3+5)