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


string = 'CATS'
x = 0


list_ = [string[i] for i in range(len(string))]
blank_list = ['_' for i in range(len(string))]



while(x<6):
    print("\nGuess an alphabet")
    guess = input()
    for i in range(len(list_)):
        if(guess == list_[i]):
            blank_list[i] = list_[i]
    if guess not in list_:
        x+=1
    if '_' not in blank_list:
        print('You won')
        break
    if guess in blank_list:
        print('You already guessed the letter..!!')
    else:
        pass
    hangman(x)
    print(' '.join(blank_list))

if(x==6):
    print('You lost..!!')
