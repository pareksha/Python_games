import random
import sys
import time

import os


def initialiseBoard():
    """Set the grid dimensions according to the user.
        Function returns grid_list containing the grid values.

        Option to change the size of the board added.
    """
    global grid_list
    size_of_grid = int(input('Enter the board size: '))
    grid_list = [['O' for _ in range(size_of_grid)] for _ in range(size_of_grid)]
    return grid_list


def printBoard(list_):
    """Prints the board after each guess.
        list_ contains the grid which is to be printed.
    """
    print('   ', end='')
    for j in range(len(list_)):
        print(str(j + 1).center(3), end='')
    print('')
    i = 1
    for column_list in list_:
        print(str(i).ljust(3), end=' ')
        for column in column_list:
            if len(column) == 1:
                print(column, end='  ')
            elif len(column) == 2:
                print(column, end=' ')
            else:
                print(column, end='')
        print('')
        i += 1
    return


def placeMouse():
    """Place the mouse at random position on the grid.
        Return the row and column number of the mouse
    """
    if player == 'User':
        mouse_row_number = random.randint(1, len(grid_list))
        mouse_column_number = random.randint(1, len(grid_list))
    else:
        print('\nInitialise row and column for the mouse : ')
        # Checking the user input
        while 1:
            mouse_row_number = int(input('Row Number: '))
            if mouse_row_number <= len(grid_list):
                break
            else:
                print('Input row out of grid. Please try again !')

        while 1:
            mouse_column_number = int(input('Column Number: '))
            if mouse_column_number <= len(grid_list):
                break
            else:
                print('Input column out of grid. Please try again !')

    return mouse_row_number, mouse_column_number


def getUserGuess():
    """Take user's guess.
        Return the guessed row and column.
    """
    # Checking the user input
    while 1:
        guess_row = int(input('Guess Row: '))
        if guess_row <= len(grid_list):
            break
        else:
            print('Input row out of grid. Please try again !')

    while 1:
        guess_column = int(input('Guess Col: '))
        if guess_column <= len(grid_list):
            break
        else:
            print('Input column out of grid. Please try again !')

    return guess_row,guess_column


def howFar(user_row, user_col, mouse_row, mouse_col):
    """Return the distance, that is, the number of vertical and
    horizontal steps to reach the mouse.
    """
    return abs(user_row - mouse_row) + abs(user_col - mouse_col)


def update_grid(user_row, user_column, distance):
    """Update the grid with the distance of the mouse
    from where the user guessed.
    """
    if distance == 0:
        grid_list[user_row - 1][user_column - 1] = 'X'
    else:
        grid_list[user_row - 1][user_column - 1] = str(distance)
    return


def input_lives():
    """Number of lives of the hunter are input by the user.

    Option to change the number of lives added.
    """
    # Checking the user input
    while 1:
        # option to change the number of lives added
        if player == 'User':
            no_of_lives = int(input('How many lives do you want? '
                                    '(Min 1, Max 10) : '))
        else:
            no_of_lives = int(input('How many lives do you want to give to me? '
                                    '(Min 1, Max 10) : '))
        if no_of_lives in range(1, 11):
            break
        else:
            print('Lives must be between 1 and 10. Please try again !')
    return no_of_lives


def user_play(opt):
    """Game Play by user.
    """
    global grid_list
    global player
    player = 'User'

    if opt == 'save':
        # loading the previous game
        try:
            variable_file = open('save_game_file.txt')
            list_variable = variable_file.read().split(',')

            n, no_of_lives, str_, \
                mouse_row, mouse_column = list_variable

            n, no_of_lives, mouse_row, mouse_column = int(n), int(no_of_lives), \
                int(mouse_row), int(mouse_column)

            list_of_grid_values = []
            x = str_.split(';')
            for y in x:
                inner_list = y.split(' ')
                list_of_grid_values.append(inner_list)

            grid_list = list_of_grid_values
        except FileNotFoundError:
            print('No save game present.')
            return

    else:
        print("\nLet's Play")
        no_of_lives = input_lives()
        list_of_grid_values = initialiseBoard()
        mouse_row, mouse_column = placeMouse()
        print()
        n = no_of_lives

    flag = True
    opt = ''
    while flag and n:
        print()
        printBoard(list_of_grid_values)
        print()
        if opt == 'new':
            # asking the user to quit or to continue
            input_ = input('Press \'q\' to \'save and quit\' or press enter '
                           '(or input anything) to continue with the game -> (q/c) :')
            if input_ == 'q':
                # loading data into file
                new_list = []
                for x in list_of_grid_values:
                    y = ' '.join(x)
                    new_list.append(y)
                str_ = ';'.join(new_list)

                variable_list = [str(n), str(no_of_lives), str_,
                                 str(mouse_row), str(mouse_column)]
                variable_string = ','.join(variable_list)
                file_ = open('save_game_file.txt', 'w')
                file_.write(variable_string)
                file_.close()
                print('Please come back again !')
                sys.exit()
        print()
        print('Guess {} out of {}...'.format(no_of_lives - n + 1, no_of_lives))
        user_guess_row, user_guess_col = getUserGuess()
        distance = howFar(user_guess_row, user_guess_col,
                          mouse_row, mouse_column)
        update_grid(user_guess_row, user_guess_col, distance)
        if distance == 0:
            print('\n')
            printBoard(list_of_grid_values)
            print('\nCongratulations ! You caught the mouse in {} moves.'
                  .format(no_of_lives - n + 1))
            flag = False
        n -= 1
        print('\n')
        opt = 'new'

    if flag:
        printBoard(list_of_grid_values)
        print('\nYou ran out of lives !\n')

    return


def computer_play():
    """Game Play by computer
    Computer can intelligently play the game.

    Role reverse feature added.
    """
    global player
    player = 'Computer'
    print("\nSee my play")

    no_of_lives = input_lives()
    list_of_grid_values = initialiseBoard()
    computer_guess_list = [(x,y) for x in range(1,len(list_of_grid_values) + 1)
                           for y in range(1,len(list_of_grid_values) + 1)]
    previous_guess_list = []
    random.shuffle(computer_guess_list)
    mouse_row, mouse_column = placeMouse()
    print()
    n = no_of_lives
    flag = True
    while flag and n:
        printBoard(list_of_grid_values)
        print('\n')
        print('Guess {} out of {}...'.format(no_of_lives - n + 1, no_of_lives))
        if n != no_of_lives:
            previous_row_guess = computer_guess_row
            previous_column_guess = computer_guess_column
            previous_guess_list.append((previous_row_guess,
                                        previous_column_guess, distance))

        for available_guesses in computer_guess_list:
            computer_guess_row, computer_guess_column = available_guesses
            if n != no_of_lives:
                num = 0
                for pre_guess in previous_guess_list:
                    if abs(computer_guess_row - pre_guess[0]) + \
                            abs(computer_guess_column - pre_guess[1]) \
                            == pre_guess[2] and \
                            list_of_grid_values[computer_guess_row - 1] \
                            [computer_guess_column - 1] == 'O':
                        num += 1
                    else:
                        break
                if num == len(previous_guess_list):
                    break
            else:
                break
        distance = howFar(computer_guess_row, computer_guess_column,
                          mouse_row, mouse_column)
        update_grid(computer_guess_row, computer_guess_column, distance)
        if distance == 0:
            print('\n')
            printBoard(list_of_grid_values)
            print('\nYeah ! I caught the mouse in {} moves.'
                  .format(no_of_lives - n + 1))
            flag = False
        n -= 1
        print()
        time.sleep(1)

    if flag:
        printBoard(list_of_grid_values)
        print('\nSorry, I ran out of lives !\n')

    return


if __name__ == '__main__':
    # Game Play
    while 1:
        option = input('Want to play new game or load the saved game (Load/New) :')
        if option in ['load', 'Load', 'LOAD']:
            # load the previous game
            user_play('save')
            try:
                os.remove('save_game_file.txt')
            except FileNotFoundError:
                pass
            input_ = input('Let\'s play a new game ! (yes/no): ')
            if input_ in ['No', 'NO', 'no']:
                print('Bye, see you next time !')
                sys.exit()
            break
        elif option in ['new', 'NEW', 'New']:
            # new game
            break
        else:
            print('Wrong Input. Try Again !')

    while 1:
        play = input('Want the computer to play and illustrate the game ? '
                     '(Yes/No) -> ')
        if play in ['Yes', 'YES', 'yes']:
            computer_play()
        elif play in ['No', 'NO', 'no']:
            user_play('new')
        else:
            print('Wrong Input. Try Again !')
            continue
        flag = True
        while flag:
            # option to play again at the end
            ans = input('Want to play again ? (Yes/No) -> ')
            if ans in ['Yes', 'YES', 'yes']:
                flag = False
            elif ans in ['No', 'NO', 'no']:
                print('Bye, see you next time !')
                sys.exit()
            else:
                print("\nWrong Input, let's try again !\n")
