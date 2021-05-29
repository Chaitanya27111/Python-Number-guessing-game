# Python-Number-guessing-game
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
