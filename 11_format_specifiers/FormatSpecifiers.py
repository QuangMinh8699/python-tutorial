# format specifiers = {:flag} format a valie based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive Value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -937.73
price3 = 12.42

print(f"price 1 is ${price1:.2f}")
print(f"price 2 is ${price2:.1f}")
print(f"price 3 is ${price3:.3f}")

print(f"price 1 is ${price1:10}")
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3:10}")

print(f"price 1 is ${price1:^10}")
print(f"price 2 is ${price2:^10}")
print(f"price 3 is ${price3:^10}")

print(f"price 1 is ${price1:+}")
print(f"price 2 is ${price2:+}")
print(f"price 3 is ${price3:+}")

print(f"price 1 is ${price1: }")
print(f"price 2 is ${price2: }")
print(f"price 3 is ${price3: }")

print(f"price 1 is ${price1:,}")
print(f"price 2 is ${price2:,}")
print(f"price 3 is ${price3:,}")
