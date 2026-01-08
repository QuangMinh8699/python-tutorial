# *args       = allows you to pass multuple non-key arguments
# **kwargs    = allows you to pass multiple keyword-arguments
#               * unpacking operator
#             1. positional 2. default 3. keyword 4. ARBITRARY

def add(*args):
    print(type(args))
    total = 0
    for arg in args:
        print(f"arg: {arg}")
        total += arg
    return total    

print(add(1, 2, 3))

def print_address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

print_address(stress="Tan Ap", city="Ha Noi", zip="12345")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    
    print()
    for key, value in kwargs.items():
        print(key, value)

    print(f"stress: {kwargs.get("stress")}")

shipping_label("Dr.", "Spongebob", "ABV", "III",
               stress="Tan Ap",
               city="Hanoi")

