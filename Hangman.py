def hangman(number):
    if(number == 0):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 1):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 2):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('|   |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 3):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('/|   |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 4):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('/|\  |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 5):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('/|\  |'.rjust(10))
        print('/    |'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 6):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('/|\  |'.rjust(10))
        print('/ \  |'.rjust(10))
        print('|'.rjust(10))
        print('='*15)

import random

list_of_strings = \
['ACRES',
 'ADULT',
 'ADVICE',
 'ARRANGEMENT',
 'ATTEMPT',
 'AUGUST',
 'AUTUMN',
 'BORDER',
 'BREEZE',
 'BRICK',
 'CALM',
 'CANAL',
 'CASEY',
 'CAST',
 'CHOSE',
 'CLAWS',
 'COACH',
 'CONSTANTLY',
 'CONTRAST',
 'COOKIES',
 'CUSTOMS',
 'DAMAGE',
 'DANNY',
 'DEEPLY',
 'DEPTH',
 'DISCUSSION',
 'DOLL',
 'DONKEY',
 'EGYPT',
 'ELLEN',
 'ESSENTIAL',
 'EXCHANGE',
 'EXIST',
 'EXPLANATION',
 'FACING',
 'FILM',
 'FINEST',
 'FIREPLACE',
 'FLOATING',
 'FOLKS',
 'FORT',
 'GARAGE',
 'GRABBED',
 'GRANDMOTHER',
 'HABIT',
 'HAPPILY',
 'HARRY',
 'HEADING',
 'HUNTER',
 'ILLINOIS',
 'IMAGE',
 'INDEPENDENT',
 'INSTANT',
 'JANUARY',
 'KIDS',
 'LABEL',
 'LEE',
 'LUNGS',
 'MANUFACTURING',
 'MARTIN',
 'MATHEMATICS',
 'MELTED',
 'MEMORY',
 'MILL',
 'MISSION',
 'MONKEY',
 'MOUNT',
 'MYSTERIOUS',
 'NEIGHBORHOOD',
 'NORWAY',
 'NUTS',
 'OCCASIONALLY',
 'OFFICIAL',
 'OURSELVES',
 'PALACE',
 'PENNSYLVANIA',
 'PHILADELPHIA',
 'PLATES',
 'POETRY',
 'POLICEMAN',
 'POSITIVE',
 'POSSIBLY',
 'PRACTICAL',
 'PRIDE',
 'PROMISED',
 'RECALL',
 'RELATIONSHIP',
 'REMARKABLE',
 'REQUIRE',
 'RHYME',
 'ROCKY',
 'RUBBED',
 'RUSH',
 'SALE',
 'SATELLITES',
 'SATISFIED',
 'SCARED',
 'SELECTION',
 'SHAKE',
 'SHAKING',
 'SHALLOW',
 'SHOUT',
 'SILLY',
 'SIMPLEST',
 'SLIGHT',
 'SLIP',
 'SLOPE',
 'SOAP',
 'SOLAR',
 'SPECIES',
 'SPIN',
 'STIFF',
 'SWUNG',
 'TALES',
 'THUMB',
 'TOBACCO',
 'TOY',
 'TRAP',
 'TREATED',
 'TUNE',
 'UNIVERSITY',
 'VAPOR',
 'VESSELS',
 'WEALTH',
 'WOLF',
 'ZOO']
string = random.choice(list_of_strings)

x = 0

list_ = [string[i] for i in range(len(string))]
blank_list = ['_' for i in range(len(string))]

hangman(0)
print(' '.join(blank_list))

while(x<6):
    print("\nGuess an alphabet")
    guess = (input()).upper()
    if len(guess) == 1:
        if guess in blank_list:
            print('You already guessed the letter..!!')
        for i in range(len(list_)):
            if(guess == list_[i]):
                blank_list[i] = list_[i]
        if guess not in list_:
            x+=1
        if '_' not in blank_list:
            print('You won')
            break
        else:
            pass
        hangman(x)
        print(' '.join(blank_list))
    else:
        print('Please enter only one character')

if(x==6):
    print('You lost..!!')
    print('Correct word is',string)
