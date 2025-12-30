# collection = single "variable" used to store multiple values
#     List = [] ordered and changeable. Duplicates OK
#     Set = {} unordered and immutable, but Add/Remove OK, NO duplicates
#     Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut", "coconut")

print(fruits)
print(len(fruits))

print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit, end="+")

for i in range(len(fruits)):
    print(fruits[i], end="-")    

# print(dir(fruits))
# print(help(fruits))
