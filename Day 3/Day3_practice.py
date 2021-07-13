# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 11:20:04 2021

@author: smwin
"""
'''#if - else Condition
if condition:
#   do this
else:
#    do this
'''
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")
    
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Grow your height above before you can ride!")
    
# <    less than 
# >    greater than
# >=   greater than or equal to
# <=   less than or equal to
# ==   equal operator

#TO CHECK EVEN OR ODD NUMBER
print("Check for ODD or EVEN")
num = int(input("Enter the number to check: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#TO CHECK PRIME OR COMPOSITE NUMBER
print("Check if a number is prime or not")
num = int(input("Enter a number to check: "))
flag = False
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break
if flag:
    print(f"{num} is not prime")
else:
    print(f"{num} is prime")

    
#NESTED IF ELSE
'''
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
'''   
#If/elif/else:
'''
if condition 1:
    do A
elif condition 2:
    do B
else:
    do C
'''

#BMI CALCULATOR 2.0
print("Welcome to the new BMI Calculator")   
weight = float(input("Enter your weight in kg: " ))
height = float(input("Enter your height in m: "))
BMI = round(weight / (height**2))
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal Weight")
elif 25 <= BMI < 30:
    print("Overweight")
elif 30 <= BMI < 35:
    print("obese")
else:
    print("clinically obese")

#IF LEAP YEAR
print("CHECK LEAP YEAR")
year = int(input("Enter the Year ex - 1990 : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
    
#Multiple if
'''
if condition 1:
    do A
if condition 2:
    do B
if condition 3:
    do C
'''
#difference between if/elif/else AND multiple if
'''
In if/elif/else only one of the given will be executed depending on the condition.
But in case of multiple if every condition is checked independent of the fact that previous 
conditiion is true or false.
'''

#Ordering Pizza
print("Welcome to Python Pizza Deliveries!")
price = 0
print("Select your Pizza:")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you wantt pepperone? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == 'S':
    price += 15
    if add_pepperoni == 'Y':
        price += 2
elif size == 'M':
    price += 20
    if add_pepperoni == 'Y':
        price += 3
elif size == 'L':
    price += 25
    if add_pepperoni == 'Y':
        price += 3
if extra_cheese == 'Y' :
    price += 1
print(price)

# Logical Operators
'''
A and B \\ A & B
A or B \\ A|B
not E
'''

'''
ASDEF.lower() #output asdef
ASEDased.count('a') #output 1 #it is case sensitive
ASEDased.lower().count('a') #output 2
'''

#LOVE CALCULATOR
his = (input("Enter his name: ")).lower()
her = (input("Enter her name: ")).lower()
t = his.count('t') + her.count('t')
r = his.count('r') + her.count('r')
u = his.count('u') + her.count('u')
e = his.count('e') + her.count('e')
sum1 = t + r + u + e
l = his.count('l') + her.count('l')
o = his.count('o') + her.count('o')
v = his.count('v') + her.count('v')
e = his.count('e') + her.count('e')
sum2 = l + o + v + e
love_score = sum1*10 + sum2

if love_score < 10 or love_score > 90:
    print(f"Your Score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your Score is {love_score}, you are alright together.")
else:
    print(f"Your Score is {love_score}")
    
    

     
    




 
    
    