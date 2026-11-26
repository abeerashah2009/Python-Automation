import sys

# Read two numbers from the command line
number1 = int(sys.argv[1])
number2 = int(sys.argv[2])

# Conditional statements with elif
if number1 > number2:
    print("Number 1 is larger")
elif number1 < number2:
    print("Number 2 is larger")
else:
    print("Both numbers are equal")
