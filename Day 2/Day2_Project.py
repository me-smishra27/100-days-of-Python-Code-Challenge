# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:37:51 2021

@author: smwin
"""
#Problem
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $\n"))
total_people = int(input("How many people to split the bill?\n"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
each_pay = round(((total_bill*(1+(tip/100)))/total_people),2)
print(f'Each person should pay: ${each_pay}')                 