import math

friends = 15
group = 2

friends += 1 # -> friends = friends + 1
friends -= 2 # -> friends = friends - 2
friends *= 3 # -> friends = friends * 3
friends /= 4 # -> friends = friends / 4


"""
**
This operator calculates the power of a number. The left operand is the base, and the right operand is the exponent.

print(2 ** 3)   # Output: 8 (2 raised to the power of 3, i.e., 2 * 2 * 2)
print(5 ** 2)   # Output: 25 (5 raised to the power of 2, i.e., 5 * 5)
"""
friends **= 5 # -> friends = friends ** 5

"""
//
This operator performs division and then truncates the result to the nearest whole number (integer) that is less than or equal to the actual result.
It effectively discards the fractional part of the division, always rounding down towards negative infinity.

print(7 // 3)   # Output: 2 (7 / 3 = 2.33..., rounded down to 2)
print(-7 // 3)  # Output: -3 (-7 / 3 = -2.33..., rounded down to -3)
"""
friends //= 6 # -> friends = friends // 5

remainder = friends % group
print(remainder)

x = -4
y = 9
z = 4.85

round = round(z)
print(f"round {round}")

absolute_value = abs(x)
print(f"x: {x}")

pow = pow(y, 2) # This is y ** 2
print(f"pow: {pow}")

max = max(z, x, y)
print(f"max: {max}")

min = min(z, x, y)
print(f"min: {min}")

print(f"pi: {math.pi}")
print(f"e: {math.e}")

square_root = math.sqrt(y)
print(f"square root: {square_root}")

ceil = math.ceil(z)
print(f"ceil: {ceil}")

floor = math.floor(z)
print(f"floor: {floor}")
