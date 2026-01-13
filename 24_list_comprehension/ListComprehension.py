# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

doubles2 = [x * 2 for x in range(1, 11)]

print(doubles2)

triples = [y * 3 for y in range(1, 11)]

print(triples)

fruits = ["apple", "banana"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1, -1, -2, 3, 4, 5]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)

negative_nums = [num for num in numbers if num < 0]
print(negative_nums)

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

odd_nums = [num for num in numbers if num % 2 != 0]
print(odd_nums)