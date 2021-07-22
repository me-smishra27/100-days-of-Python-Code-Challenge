# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Find the factorial of number

#Using Built in Function
num = int(input("Enter the Number to find factorial: "))
import math
fact = math.factorial(num)
print(fact)


#Using Recursion Method
def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)
print(fact(num))

#Using While loop
fact = 1
if num < 0:
    print("Enter a positive number: ")
if num > 0:
    while num > 0:
        fact *= num
        num -= 1
    print(fact)
    
    
#Using for loop
x = int(input("Enter the number"))
fact = 1
for i in range(x, 0, -1):
    fact = fact * i
print(fact)

        