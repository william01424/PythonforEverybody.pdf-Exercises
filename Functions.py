print(type(2673))

# Built-in Function Examples

print(max('Hello world'))
print(min('Hello world'))           # min is ' '
print(len('Hello world'))

# Type Conversion Functions

int('24')
# int('Number')

int(2.888978)
int(-2.353)

# Can also use float() and str() for other conversions

# Math Functions

import math
print(math)

# radians = 0.43
# height = math.sin(radians)
# print(height)

deg = 45
rad = (deg / 360) * 2 * math.pi
print(math.sin(rad), end='\n\n')

# Random Numbers

import random
for i in range(10):
    x = random.random()
    print(x)

# Note: the random function returns a random float between 0.0 and 1.0 **including 0.0 but not 1.0

print(random.randint(5,10))
print(random.randint(5,10))

t = [1,2,3]
print(random.choice(t))
print(random.choice(t))