def calculatepay(x, y):  # This function calculates their pay

    if x <= 40:
        return (x * y)
    overtime = x - 40
    return ((40 * y) + (1.5 * y * overtime))


def checkfloat(inputnumber):  # This function ensures they enter a variable that can be a float.
    try:
        number = float(inputnumber)
        return number
    except ValueError:
        print('Error please enter numeric input')
        quit()



hours = input('Enter Hours: ')  # Getting user inputs, then running checkfloat and setting to a new variable x1/y1
x1 = checkfloat(hours)

rate = input('Enter Rate: ')
y1 = checkfloat(rate)

# Final output - formatted to 2sf. (Uses float checked vars x1/y1)
print('Pay: ', "{:.2f}".format(calculatepay(x1, y1)))



def checkbad(score):
    try:
        x = float(score)
        if x < 0 or x > 1:
            print('Please enter a valid score between 0 and 1.')
            quit()
        else:
            return x
    except ValueError:
        print("Value Error - Enter a number not a word.")
        quit()

def gradescore(x):
    if x >= 0.9:
        print('A')
    elif x >= 0.8:
        print('B')
    elif x >= 0.7:
        print('C')
    elif x >= 0.6:
        print('D')
    else:
        print('F')

inputscore = input('Please enter your score from 0.0 to 1.0: ')
checkedscore = checkbad(inputscore)
gradedscore = gradescore(checkedscore)

