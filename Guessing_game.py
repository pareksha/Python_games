'''Guess the number game'''

import random
right_guess = random.randint(1,20)
flag = False
print("Guess a number between 1 and 20")


for i in range(0,3):
    if(flag == False):
        input_number = int(input())
        if(input_number == right_guess):
            print("You guessed right!")
            print("You won..!!")
            flag = True
        else:
            print("Try Again!")
            print("You have {} turn(s) left..!!".format(2-i))

if(flag == False):
    print("You lost..!\nBetter luck next time...!!")
