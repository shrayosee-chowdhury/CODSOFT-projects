# CALCULATOR
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.


n1 = (float(input("ENTER YOUR 1ST NUMBER :")))
n2 = (float(input("ENTER YOUR 2ND NUMBER :")))
operators = input ("ENTER ANY OPERATOR (+, -, *, /) :")

if operators == "+":
    result = n1 + n2
    print (result)
elif operators == "-":
    result = n1 - n2
    print (result)
elif operators == "*":
    result = n1 * n2
    print (result)
elif operators == "/":
    result = n1 / n2
    print (result)
    
    