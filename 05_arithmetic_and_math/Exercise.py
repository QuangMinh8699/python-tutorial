import math

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
print(f"The circumference is {round(circumference, 2)}")
print(f"The area of the circle is {round(area, 2)}")