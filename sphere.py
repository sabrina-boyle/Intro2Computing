"""
Program: Sphere
Author: sabsing

This program calculates the equations of a sphere by using a user inputed radius.

Inputs: The radius of a sphere as a floating-point number
Outputs: The calculated diameter, circumference, surface area, and volume
"""
import math

# User inputs the radius
radius = float(input("Enter the sphere's radius: "))
print("")
# Calculate the diameter
diameter = 2*radius
print("Diameter      :", round(diameter,2))

# Calculate the circumference
circumference = diameter*math.pi
print("Circumference :", round(circumference,2))

# Calculate the surface area
surfaceArea = 4*math.pi*radius**2
print("Surface area  :", round(surfaceArea,2))

# Calculate the volume
volume = (4/3)*math.pi*radius**3
print("Volume        :", round(volume,2))
