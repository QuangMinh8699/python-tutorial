# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 36
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else: 
    print("The outdoor event is still scheduled")

###

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is Hot")
elif temp <= 0 and not is_sunny:
    print("It is Cold")
