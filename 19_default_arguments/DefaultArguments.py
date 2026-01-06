# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your function more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount = 0, tax = 0): # --> default arguments
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))

def count(end, start = 0):
    for x in range(start, end + 1):
        print(x)
    print("DONE")

count(5)