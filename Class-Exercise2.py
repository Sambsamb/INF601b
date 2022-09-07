"""
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
Expected Output:
Vehicle Name: School Volvo Speed: 180 Mileage: 12
"""


# Parent Class definition
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


# Child Class definition:
class Bus(Vehicle):

    def __str__(self):
        return f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"


# Child Class usage:
volvo = Bus("School Volvo", 180, 12)
print(volvo)

