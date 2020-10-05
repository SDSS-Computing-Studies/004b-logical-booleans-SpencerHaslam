#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)
Inputs:
an integer
an integer
an integer
Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple
Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple
Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
number1 = int(input("Enter an interger"))
number2 = int(input("Enter an interger"))
number3 = int(input("Enter an interger"))
maxval = max(number1, number2, number3)
minval = min(number1, number2, number3)
midval = (number1 + number2 + number3) - (maxval + minval)
sqmin = minval ** 2
sqmid = midval ** 2
sqmax = maxval ** 2
firsthalf = sqmin + sqmid
if firsthalf == sqmax:
    snumber1=  str(minval)
    snumber2 = str(midval)
    snumber3 = str(maxval)
    print(snumber1 + "," + snumber2 + "," + snumber3 + " form a Pythagorean triple")
else:
    snumber1 = str(minval)
    snumber2 = str(midval)
    snumber3 = str(maxval)
    print(snumber1 + "," + snumber2 + "," + snumber3 + " do not form a Pythagorean triple")
