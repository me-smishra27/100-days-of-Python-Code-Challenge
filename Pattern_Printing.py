# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:13:20 2021

@author: smwin
"""

#Pattern Printing
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

nr = int(input("Enter the number of rows: "))
for i in range(1, nr+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
#Pattern Printing
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
nr = int(input("Enter the number of rows: "))
for i in range (1, nr+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
    
#Pattern Printing 
#FLOYDS TRIANGLE
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''

nr = int(input("Enter the number of rows: "))
num = 1
for row in range(1, nr+1):
    for colm in range(1,row+1):
        print(num, end=" ")
        num += 1
    print()
    
#Pattern Printing
#Reverse Floyds Triangle
'''
15  
14  13  
12  11  10  
9   8   7   6   
5   4   3   2   1  
'''

nr = int(input("Enter the number of rows: "))
k = 0
for i in range(nr):
    k += i
m = nr + k
for i in range(1,nr+1):
    for j in range(1, i+1):
        print(format(m, "<3"), end=' ')
        m -= 1
    print()
    
#Pattern Printing
# Hollow Right Triangle
'''
*         
**        
* *       
*  *      
*   *     
*    *    
*     *   
*      *  
*       * 
**********
'''
nr = int(input("Enter the number of rows: "))
for i in range(nr):
    for j in range(nr):
        if i == nr-1 or j == 0 or i == j:
            print("*", end="")
        else:
            print(end=" ")
    print()

#Pattern Printing
'''
*****
 *  *
  * *
   **
    *
'''
nr = int(input("Enter the number of rows: "))
for i in range(nr):
    for j in range(nr):
        if i == 0 or j == nr-1 or i == j:
            print("*", end="")
        else:
            print(end = " ")
    print()
