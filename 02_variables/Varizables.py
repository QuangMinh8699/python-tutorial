# Variable = A container for a value (string, integer, ...)
#            A variable behaves as if it was the value it contains 

#string
first_name = "Minh"
food = "pizza"

print(first_name)
print(f"Hello {first_name}")
print(f"I like {food}")

#integer
age = 25
quantity = 3

print(f"I am {age} years old")
print(f"I am buying {quantity} items")

#float
price = 10.99
gpa = 3.2

print(f"The price is {price}")
print(f"My GPA is {gpa}")

#boolean
is_student = True

print("Are you student ?")
if is_student:
    print("Yes, I am a student")
else:
    print("No, I'm not")