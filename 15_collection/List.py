# collection = single "variable" used to store multiple values
#     List = [] ordered and changeable. Duplicates OK
#     Set = {} unordered and immutable, but Add/Remove OK, NO duplicates
#     Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "banana", "orange", "coconut", "banana"]

print(fruits[::2])
print(len(fruits))
print("apple" in fruits)
print("pineapple" in fruits)

fruits.append("pineapple")
for i in range(len(fruits)):
    print(fruits[i])

fruits.remove("apple")
print(fruits)

fruits.insert(0, "apple")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.index("apple"))

print(fruits.count("banana"))

fruits.clear()
print(fruits)

print(dir(fruits))
print(help(fruits))

