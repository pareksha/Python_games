import time
import sys

board = [' ' for i in range(9)]

def frame():
    print('|   |'.center(11) + ' '*10 + '|   |'.center(11))
    print(board[6].center(3) + '|' + board[7].center(3) + '|' + board[8].center(3) + ' '*10 + '7'.center(3) + '|' + '8'.center(3) + '|' + '9'.center(3))
    print('|   |'.center(11) + ' '*10 + '|   |'.center(11))
    print('-'*11 + ' '*10 + '-'*11)
    print('|   |'.center(11) + ' '*10 + '|   |'.center(11) )
    print(board[3].center(3) + '|' + board[4].center(3) + '|' + board[5].center(3) + ' '*10 + '4'.center(3) + '|' + '5'.center(3) + '|' + '6'.center(3))
    print('|   |'.center(11) + ' '*10 + '|   |'.center(11))
    print('-'*11 + ' '*10 + '-'*11)
    print('|   |'.center(11) + ' '*10 + '|   |'.center(11))
    print(board[0].center(3) + '|' + board[1].center(3) + '|' + board[2].center(3) + ' '*10 + '1'.center(3) + '|' + '2'.center(3) + '|' + '3'.center(3))
    print('|   |'.center(11) + ' '*10 + '|   |'.center(11))

def player_input():
    frame()
    print('What is your next move ? (1-9)')
    move = int(input()) - 1
    while(board[move] != ' '):
        print('The slot is already filled.. Try Again.. !!')
        move = int(input()) - 1
    board[move] = 'X'
    frame()


def computer_input():
    print('Let the computer play..')
    time.sleep(1)

def move(list_):
    for i in range(len(list_)):
        if(board[list_[i][0]] == 'O' and board[list_[i][1]] == 'O' and board[list_[i][2]] == ' '):
            board[list_[i][2]] = 'O'
            frame()
            print('You lost..!!')
            sys.exit()
        elif(board[list_[i][1]] == 'O' and board[list_[i][2]] == 'O' and board[list_[i][0]] == ' '):
            board[list_[i][0]] = 'O'
            frame()
            print('You lost..!!')
            sys.exit()
        elif(board[list_[i][0]] == 'O' and board[list_[i][2]] == 'O' and board[list_[i][1]] == ' '):
            board[list_[i][1]] = 'O'
            frame()
            print('You lost..!!')
            sys.exit()
    for i in range(len(list_)):
        if(board[list_[i][0]] == 'X' and board[list_[i][1]] == 'X' and board[list_[i][2]] == ' '):
            board[list_[i][2]] = 'O'
            break
        elif(board[list_[i][1]] == 'X' and board[list_[i][2]] == 'X' and board[list_[i][0]] == ' '):
            board[list_[i][0]] = 'O'
            break
        elif(board[list_[i][0]] == 'X' and board[list_[i][2]] == 'X' and board[list_[i][1]] == ' '):
            board[list_[i][1]] = 'O'
            break
        else:
            pass

#play
print('Computer will play first..')
board[6] = 'O'
player_input()
computer_input()

list_ = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]
list_1 = [0,1,2,3,4,5,6,7,8]


if(board[2] == ' '):
    board[2] = 'O'
    player_input()
    computer_input()


    flag_ = False


    move(list_)


    player_input()
    computer_input()
    move(list_)
    player_input()
    computer_input()

    for x in list_1:
        if(board[x] == ' '):
            board[x] = 'O'
            frame()
    for i in range(len(list_)):
        if(board[list_[i][0]] == 'O' and board[list_[i][1]] == 'O' and board[list_[i][2]] == 'O'):
            print('You lost..!!')
            flag_ = True
    for i in range(len(list_)):
        if(board[list_[i][0]] == 'X' and board[list_[i][1]] == 'X' and board[list_[i][2]] == 'X'):
            print('You Won..!!')
            flag_ = True
    if(flag_ == False):
        print('Game is DRAW..!!')


elif(board[2] == 'X'):
    board[8] = 'O'
    player_input()
    computer_input()

    move(list_)
    board[0] = 'O'
    player_input()
    computer_input()
    move(list_)

else:
    pass
