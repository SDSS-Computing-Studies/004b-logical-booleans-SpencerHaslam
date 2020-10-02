#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math

# Taking the input from user
number = int(input("Enter a Number"))

root = math.sqrt(number)
qroot = (number **(1/3))
qroot = round(qroot, 10)
print(qroot)
print(root**2, qroot**3)
if root ** 2 == number and qroot ** 3 == number :
    print(number, " is both a perfect square and a perfect cube.")
elif root ** 2 == number:
    print(number,  "is only a perfect square.")
else:
    print(number, " is only a perfect cube.")
