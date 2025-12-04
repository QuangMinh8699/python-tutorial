# input() = A function that prompts the user to enter data
#           returns the entered data as a string

name = input("What is your name ?: ")
age = input("How old are you ?")

print(f"Hello {name} !")
print(f"the type of the age variable is {type(age)}")
print(f"You are {age} years old !")

age = int(age)
age += 1
print(f"You are {age} years old next year")

# Exercise 1 rectangle area Calc
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is {area} m²")