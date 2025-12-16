name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")

print(f"length: {len(name)}")

print(f"The letter 'm' is in the {name.find("m")} position")

print(f"Capitalize: {name.capitalize()}")

print(f"UpperCase: {name.upper()}")

print(f"LowerCase: {name.lower()}")

print(f"isDigit: {name.isdigit()}")

print(f"isAlpha: {name.isalpha()}")

print(f"Your phone number has: {phone_number.count("-")} - letters")

print(help(str))

