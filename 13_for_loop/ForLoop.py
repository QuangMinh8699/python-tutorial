# for loop = execute a block of code a fixed number of times
#            you can iterate over a range, string, sequence, etc


import time


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds}")
    time.sleep(1)

for x in range(1, 11):
    print(x)

for x in range(1, 11, 2):
    print(x)

for x in reversed(range(1, 11)):
    print(x)

print("end")