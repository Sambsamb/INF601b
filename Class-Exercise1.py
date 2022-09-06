"""
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""


# Class definition:
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# Class usage:
mercedes = Vehicle(150, 33)
print("Mercedes: max_speed", mercedes.max_speed, ", mileage", mercedes.mileage)
