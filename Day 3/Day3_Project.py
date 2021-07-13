# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 00:41:36 2021

@author: smwin
"""
print('''
       _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
      ''')
print("Welcome to the Treausre Island \n")
print("Your mission is to find the treasure \n")
turn = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ")
turn = turn.lower()
if turn == 'left':
    s_w = input("You come to a lake. There is an island in the middle of the lake. type 'wait' to wait for a boat or tyr 'swim' to swim across.")
    s_w = s_w.lower()
    if s_w == 'wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors. Red, Yellow and blue. Which color do you choose?  ")
        door = door.lower()
        if door == 'yellow':
            print("You Won")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
        
    
