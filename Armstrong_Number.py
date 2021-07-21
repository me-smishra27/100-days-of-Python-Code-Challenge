# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 00:50:03 2021

@author: smwin
"""

##ARMSTRONG NUMBER number of n digit which are equal to sum of nth power of its digits 
#e.g: num = 5 n( number of digit) = 1 num^n = 5^1 = 5 if num^n = num then it is armstrong number. 
#e.g: num = 13 n = 2 now sum of num^n = 1^2 + 3^2 = 10 sum of num^n != num therefore 13 is not a armstrong number.

#To get all the Armstrong number in the given range
num = int(input("Enter the range:\n"))
for i in range(num):
    temp = i
    sum1 = 0
    n = len(str(i))
    while i > 0:
        unit = i % 10 
        sum1 += unit**n
        i = i // 10
    if temp == sum1:
        print(temp)
        
#To check if the given number is Armstrong        
num2 = int(input("Enter number to check: \n"))
n = len(str(num2))
sum2 = 0
temp1 = num2
while temp1 != 0:
    unit1 = temp1 % 10
    sum2 += unit1 ** n
    temp1 = temp1//10
if num2 == sum2:
    print(f"{num2} is armstrong")
else:
    print(f"{num2} is not armstrong")
    