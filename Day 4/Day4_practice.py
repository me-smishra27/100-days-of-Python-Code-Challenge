# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 23:30:12 2021

@author: smwin
"""
#RANDOMISATION
'''It is important when program have a degree 
of unpredictibility e.g. games
#Python has an inbuilt random module
'''

import random 
random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random() # always generate float number between 0 and 1.
print(random_float)

num = random.randint(0,1)
print(num)
if num == 1:
    print("Head")
else:
    print("Tail")
    
# List ~ A data structure in python
#list is stored inside [ ]
#list is an ordered data
states_of_america = ["Delaware", "Pennsylvania", ]

#indexing list_name[start : step : stop]
print(states_of_america[0])

#list are muttable
states_of_america[1] = "Penn"
print(states_of_america)

#add item to list
states_of_america.append("Ny")
print(states_of_america)

#select random names from the given names
names = input("Enter the names of people separated by comma and space: ")
my_list = names.split(", ")
num = random.randint(0, (len(my_list)-1))
print(my_list[num])

#Nested List
list1 = 'A B C D E'.split(' ')
list2 = 'F G H I J'.split(' ')
nes_list = [list1, list2]
print(nes_list)
#OUTPUT [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'J']]
#these are list inside list

#Treasure Map
row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure")
map[int(position[0])-1][int(position[1])-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")

