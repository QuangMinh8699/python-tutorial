# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.", 
            "Vietnam": "Hanoi", 
            "India": "New Delhi", 
            "Russia": "Moscow"}

print(capitals.get("Vietnam")) # --> Hanoi
print(capitals.get("Japan")) # --> None
print(capitals.keys()) # --> dict_keys(['USA', 'Vietnam', 'India', 'Russia'])

capitals.update({"Germany": "Berlin"})
print(capitals)

for key, value in capitals.items():
    print(f"{key}: {value}")

# capitals.pop("India") # -> Pop object by key
# capitals.popitem() # -> pop last object
# capitals.clear() # --> Clear all


# print(dir(capitals))
# print(help(capitals))