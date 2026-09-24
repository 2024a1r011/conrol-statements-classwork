# Write a python program to store two points as tuples and calculate the distance between them

import math

point1 = (2, 3)
point2 = (7, 8)

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")

x1, y1 = point1
x2, y2 = point2

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Distance between the points: {distance:.4f}")