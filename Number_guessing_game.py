#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:07:35 2021

@author: Chaitanya Chhichhia

Description: A number guessing game where the user tries to guess the randomly 
             generated number in minimum turns. 
             There are two ways the game can end- 
             a) If the user guesses the number correctly
             b) If the user quits the game by typing 101
             
             RULES-
             a) The game generates number between 0 to 100 (including 0 and 100), 
             hence the user is allowed to imput only the number in the range 
             [0,100].
             b) If in the first turn, the absolute difference between your number
             and the generated number is less than or equal to 10, the console
             displays "WARM :)" else it displays "COLD :("
             c) In the subsequent turns if yout guess is nearer to your previous
             guess, than the console displays "WARMER :)" else it displays "COLDER :("
"""
import random

######## generating the random no. to be guessed ##########
goal=random.randint(0,100)
#print (goal)  #uncomment this if you want to verify the randomly generated number

###### game_play ##########

num=int (input("Enter a number :"))
i=1                                 #number of turn/s counter

if (num>101 or num<0):
    print("Enter a valid number.")
elif num==goal:
    print("Great Luck!! You have guessed the number in a single turn.")
elif abs(num-goal)<=10:
    print ("WARM :)")
else:
    print("COLD :(")
    
    
while (num!=101):
    
    i+=1
    num_initial=num
    num=int (input("Enter a number :"))
    
    if (num>101 or num<0):
        print("Enter a valid number.")
    elif num==goal:
        print("Congratulations! You have guessed the number in {} turns".format(i))
        break
    elif abs(num-goal)<abs(num_initial-goal):
        print("WARMER :)")
    else:
        print("COLDER :(")