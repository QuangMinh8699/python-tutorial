# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), ...

name = "Minh"
empty_string = ""
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
age = float(age)
is_student = str(is_student)
name = bool(name)
empty_string = bool(empty_string)

print(gpa)
print(age)
print(name)
print(empty_string)
print(type(is_student))