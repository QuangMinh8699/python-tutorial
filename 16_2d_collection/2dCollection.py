fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0][0])
print(groceries[1][2])
# print(groceries[1][3]) -> ERROR

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()