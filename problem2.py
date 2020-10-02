#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
number = float(input("Enter a number"))
number2 = float(input("Enter another number"))
maxval = max(number, number2)
minval = min(number, number2)
total = float(maxval / minval)
Itotal = int(total)
if total == Itotal:
    print(minval, "is a factor of", maxval)

else:
    print(minval, "is not a factor of", maxval)
