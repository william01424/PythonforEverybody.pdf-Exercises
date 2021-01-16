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

# Adding new functions into Python

# def is the keyword that indicates that this is a function definition.
# parentheses indicate that this particular function doesn't take inputs

def print_song():
    print("I'm burning baby, im burning up!")
    print("Im burning alive and yet I still love you.")
print_song()

def repeat_song():
    print_song()
    print_song()
repeat_song()

def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('bruce')
print_twice('spam')
print_twice('17274')


print_twice('spam '*4)          # Here - the code is going to print spam\n spam\n, multiplying each line by 4

print_twice(math.cos(math.pi))

# An example here of how a variable can be used as an argument:

William = 'William is a seriously cool dude.'
print_twice(William)

# Fruitful and Void Functions

# When calling a fruitful function - you will almost always want to do something with it

radians = 0.7

x = math.cos(radians)
golden = (math.sqrt(5) + 1)/2

# If you call a function in a script and do not store - the result disappears!?!?! MADNESS

math.sqrt(3) # - result is computed but not stored, therefore not useful

# Void functions may display something on the screen or have another effect, but they don't return a value
# Try assigning the result to a variable and see what you get

result = print_twice('Bing')

print(result)

# This brings us on to how to return a result from a function - using the return statement

def addtwonumbers(a, b):
    added = a+b
    return added

x = addtwonumbers(5,10)
print(x)

# Steps of this simple program to add two numbers:
# Computes the sum of the 2 values given
# Placed this value in the local variable which is called added
# Then return statement is used to send the computed value back to the calling code as the function result
# This was assigned to variable x then printed

def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()
