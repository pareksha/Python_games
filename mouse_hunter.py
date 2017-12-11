import random
import sys


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
        mouse_row_number = int(input('Row Number: '))
        mouse_column_number = int(input('Column Number: '))
    return mouse_row_number, mouse_column_number


def getUserGuess():
    """Take user's guess.
        Return the guessed row and column.
    """
    x = 1
    while(x):
        guess_row = int(input('Guess Row: '))
        if guess_row <= len(grid_list):
            x = 0
        else:
            print('Input row out of grid. Please try again !')
    x = 1
    while(x):
        guess_column = int(input('Guess Col: '))
        if guess_column <= len(grid_list):
            x = 0
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
    x = 1
    while x:
        # option to change the number of lives added
        if player == 'User':
            no_of_lives = int(input('How many lives do you want? '
                                    '(Min 1, Max 10) : '))
        else:
            no_of_lives = int(input('How many lives do you want to give to me? '
                                    '(Min 1, Max 10) : '))
        if no_of_lives in range(1, 11):
            x = 0
        else:
            print('Lives must be between 1 and 10. Please try again !')
    return no_of_lives


def user_play():
    """Game Play by user.
    """
    global player
    player = 'User'
    print("\nLet's Play")

    no_of_lives = input_lives()
    list_of_grid_values = initialiseBoard()
    mouse_row, mouse_column = placeMouse()
    print()

    n = no_of_lives
    flag = True
    while flag and n:
        printBoard(list_of_grid_values)
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

    if flag:
        printBoard(list_of_grid_values)
        print('\nYou ran out of lives !\n')

    return


def computer_play():
    """Game Play by computer
    """
    global player
    player = 'Computer'
    print("\nSee my play")

    no_of_lives = input_lives()
    list_of_grid_values = initialiseBoard()
    computer_guess_list = [(x,y) for x in range(1,len(list_of_grid_values) + 1)
                           for y in range(1,len(list_of_grid_values) + 1)]
    random.shuffle(computer_guess_list)
    mouse_row, mouse_column = placeMouse()
    print()
    n = no_of_lives
    flag = True
    dist = random.randint(1, len(list_of_grid_values))
    while flag and n:
        printBoard(list_of_grid_values)
        print('\n')
        print('Guess {} out of {}...'.format(no_of_lives - n + 1, no_of_lives))
        if n != no_of_lives:
            previous_row_guess = computer_guess_row
            previous_column_guess = computer_guess_column

        for tuple_ in computer_guess_list:
            computer_guess_row, computer_guess_column = tuple_
            if n != no_of_lives:
                if abs(computer_guess_row - previous_row_guess) + \
                        abs(computer_guess_column - previous_column_guess) == distance\
                        and list_of_grid_values[computer_guess_row - 1] \
                        [computer_guess_column - 1] == 'O':
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

    if flag:
        printBoard(list_of_grid_values)
        print('\nSorry, I ran out of lives !\n')

    return


if __name__ == '__main__':
    while 1:
        play = input('Want the computer to play and illustrate the game ? '
                     '(Yes/No) -> ')
        if play == 'Yes':
            computer_play()
        elif play == 'No':
            user_play()
        else:
            print('Wrong Input. Try Again !')
            continue
        flag = True
        while flag:
            # option to play again at the end
            ans = input('Want to play again ? (Yes/No) -> ')
            if ans == 'Yes':
                flag = False
            elif ans == 'No':
                print('Bye, see you next time !')
                sys.exit()
            else:
                print("\nWrong Input, let's try again !\n")
