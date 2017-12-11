import random
import sys


def initialiseBoard():
    global grid_list
    size_of_grid = int(input('Enter the board size: '))
    grid_list = [['O' for _ in range(size_of_grid)] for _ in range(size_of_grid)]
    return grid_list


def printBoard(list_):
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
    mouse_row_number = random.randint(1, len(grid_list))
    mouse_column_number = random.randint(1, len(grid_list))
    return mouse_row_number, mouse_column_number


def getUserGuess():
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
    return abs(user_row - mouse_row) + abs(user_col - mouse_col)


def update_grid(user_row, user_column, distance):
    if distance == 0:
        grid_list[user_row - 1][user_column - 1] = 'X'
    else:
        grid_list[user_row - 1][user_column - 1] = str(distance)
    return


def main():
    print("\nLet's Play")
    x = 1
    while x:
        no_of_lives = int(input('How many lives do you want? (Min 1, Max 10) : '))
        if no_of_lives in range(1, 11):
            x = 0
        else:
            print('Lives must be between 1 and 5. Please try again !')

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
        # print(mouse_row, mouse_column)
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

    # print(user_guess_row, user_guess_col)


if __name__ == '__main__':
    while 1:
        main()
        flag = True
        while flag:
            ans = input('Want to play again ? (Yes/No) -> ')
            if ans == 'Yes':
                flag = False
            elif ans == 'No':
                print('Bye, see you next time !')
                sys.exit()
            else:
                print("\nWrong Input, let's try again !\n")
