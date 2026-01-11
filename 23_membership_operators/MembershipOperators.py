# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

for i in word:
    if "A" in word:
        print("A")
    else:
        print("B")

students = {"Minh", "Nhi"}

if "Linh" not in students:
    print("Linh is not a student")
else:
    print("Linh is a student")
