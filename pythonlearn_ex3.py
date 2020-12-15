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


