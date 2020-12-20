# 1
x = float(input("Enter your hours worked:\n"))
y = float(input("Enter your hourly rate:\n"))

if x > 40:
    high_rate_hours = float(x - 40)
    bonus_rate_pay = float(high_rate_hours * y * 1.5)
    print("Your total pay (including bonus rate over 40 hours) is: £", "{:.2f}".format(((40 * y) + bonus_rate_pay)))
else:
    x <= 40
    base_rate_pay = float(x * y)
    print("Your total pay earned is: £", "{:.2f}".format(base_rate_pay))


# 2 - Adding in error message using try / except

try:
    x = float(input("Enter your hours worked:\n"))
    y = float(input("Enter your hourly rate:\n"))
except ValueError:
    print("Error, please enter a numeric input")
    quit()

    if x > 40:
        high_rate_hours = float(x - 40)
        bonus_rate_pay = float(high_rate_hours * y * 1.5)
        print("Your total pay (including bonus rate over 40 hours) is: £", "{:.2f}".format(((40 * y) + bonus_rate_pay)))
    else:
        x <= 40
        base_rate_pay = float(x * y)
        print("Your total pay earned is: £", "{:.2f}".format(base_rate_pay))
        
# 3

try:
    score = float(input("Enter your score between 0.0 and 1.0\n"))
    if score <= 0.0 or score >= 1.0:
        raise ValueError
except ValueError:
    print("Bad Score")
    quit()

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    score < 0.6
    print("F")
