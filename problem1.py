
#! python3
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""
number = float(input("Enter a Number"))
numberdiv6 = float(number / 6)
numberdiv8 = float(number / 8)
Inumberdiv6 = int(numberdiv6)
Inumberdiv8 = int(numberdiv8)

if numberdiv6 == Inumberdiv6:
    if numberdiv8 == Inumberdiv8:
        print(number, " is not frue")
    else:
        print(number, " is frue")
else:
    print(number, " is not frue")
