from Car import Car

car1 = Car("Camry", 2024, "black", True)
car2 = Car("Honda", 2025, "blue", False)

print(car1.model)
print(car2.color)

car1.drive()
car2.stop()