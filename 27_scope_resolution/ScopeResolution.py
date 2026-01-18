# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a)

def func2():
    b = 1
    # print(a) # --> ERROR

# -> a and b is local variables

def func3():
    c = 3
    def func4():
        print(c)
    func4()

# -> c is enclosed variable

d = 4
def func5():
    print(d)

# -> d is global variable

from math import e

def func6():
    print(e)

# -> e is built-in variable