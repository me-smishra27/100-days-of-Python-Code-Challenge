# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:08:21 2021

@author: smwin
"""
#1. Create a greeting for your Program
print('Welcome to the Band Name Generator.')
#2. Ask the user for the city that they grew up in.
city_name = input("What is the name of the city you grew up in?\n")
#3. Ask the user for the name of their pet.
pet_name = input("What's your pet name?\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city_name +' '+ pet_name
print(f'Your band name could be {band_name}')
#5. Make sure the input cursor shows on a new line. 