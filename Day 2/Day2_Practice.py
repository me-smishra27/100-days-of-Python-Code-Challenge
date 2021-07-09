# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:46:43 2021

@author: smwin
"""
#DATA TYPES

#String
#Indexing start from 0
print("Hello"[0]) #output H
print("12345"[4]) #output 5

#Integer
print(123 + 456) #output 579

#Float
print(3.1256) #output 3.1256
#type() is used to find the data type of any input.
print(type('23')) #output <class 'str'> 
print(type(123)) #output <class 'int'>
print(type(123.256)) #output <class 'float'>

#123_456 = 123456
print(735_529.678) #output 735529.678

num_char = len(input('What is your name?'))
#print("Your name has" + num_char + "characters")
#this will give a type error as we are trying to concatenate string with int.

#we can use type casting or conversion
new_num_char = str(num_char) 
print("Your name has " + new_num_char + " characters")

print(70 + float("100.5")) #output 170.5
print(str(70) + str(100)) #output 70100

#Exercise 1
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
num = input("Enter the two digit number: ")
a = int(num[0])
b = int(num[1])
sum = a+b
print(sum)

#Mathematical Operations
print(3+5)  #addition output 8
print(7-4)  #substraction output 3
print(3*2)  #multiplication output 6
print(6/3)  #division output 2.0 (type ~ float)
print(6//3) #floor_division output 2 (type ~ int)  
print(2**3) #exponential output 8
print(7%2)  #modulus output 1 (returns remainder)

#Priority of operations
#PEMDAS or BODMAS
#(), **, *, /, +, -

#Exercise 2
#BMI Calculator
#BMI = weight(kg)/height^2(m^2)
weight = float(input("Enter your Weight in kg: "))
height = float(input("Enter your height in m: "))
BMI = weight//(height**2)
print(f"Your BMI is {BMI}")

#f-string
score = 2
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")

#Exercise 3
total_days = 90*365
total_week = 90*52
total_months = 90*12
current_age = int(input("Enter your current age: "))
days_spent = 365*current_age
week_spent = 52*current_age
months_spent = 12*current_age
days_left = total_days - days_spent
week_left = total_week - week_spent
months_left = total_months - months_spent
print(f"You have {days_left} days, {week_left} weeks, and {months_left} months left.")

#OR
years_remaining = 90 - current_age
days_left1 = years_remaining*365
week_left1 = years_remaining*52
months_left1 = years_remaining*12
print(f"You have {days_left1} days, {week_left1} weeks, and {months_left1} months left.")


