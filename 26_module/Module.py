# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

#import math # -> import module "math"
import math as m # -> print(m.pi)
from math import pi # -> print(pi) 
from math import e # -> print(e)

import Example as example

result = example.cube(2)
print(result)
