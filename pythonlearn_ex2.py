# PythonLearn.pdf

# Chapter 2 Exercises

# 2
name = input("Enter your name\n")
print("Hello", name, '!')

# 3
hours = float(input("Enter Hours:\n"))
rate = float(input("Please enter your pay rate:\n"))


print("Your gross pay for specified hours:", "{:.2f}".format((hours * rate)))

# 4
width = 17
height = 12.0

print(width//2)         # int
print(width/2.0)        # float as float in calc changes int to float for accuracy
print(height/3)         # float/int = float
print(1 + 2 * 5)        # BODMAS applies in python

# 5 Write a program which prompts the user for a Celsius temp - converts to Fahrenheit, then print out new convert

celsius = int(input("What is the temperature in Celsius? (oC)\n"))

fahrenheit = float(((celsius * (9/5)) + 32))

print("Here is the temperature converted into degrees Fahrenheit:", "{:.2f}".format(fahrenheit), "oF",
      "(2 decimal places)")


