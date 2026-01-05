# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name: str):
    print(f"Happy Birthday {name}")

happy_birthday("Minh") # --> Happy Birthday Minh

def log(message: str) -> str:
    return "Log: " + message

print(log("Message")) # --> Log: Message