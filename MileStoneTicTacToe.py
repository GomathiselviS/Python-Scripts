# -*- coding: utf-8 -*-
"""
TicTacToe
@author: atg
"""
import random

def display_board(board):
    for i in range(0,7,3):
        print('{} | {} | {} '.format(board[i],board[i+1],board[i+2]))
        print('________')
        
def player_input():
    marker=input("Enter your choice of Marker " )
    while marker not in ['O','X']:
        print("Valid Markers are O,X")
        marker=input("Enter your choice of Marker " )
    print("You have chosen {}".format(marker))
    return marker

def player_position():
    position=int(input("Where do you want to place your marker "))
    while position >9 or position <1 :
        print("Valid Postions are: 1-9")
        position=int(input("Where do you want to place your marker "))
    position=int(position)
    return position
        
def place_marker(board,marker,position):
    board[position-1]=marker
    print(board)
    display_board(board)
    return board
      

def win_check(board,marker):
    win_list=[[1,5,9],[3,5,7],[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9]]
    present_list = [index+1 for index,val in enumerate(board) if val == marker ]
    present_list.sort()
    print(present_list)
    for w in win_list:
        result = [True if w_el in present_list else False for w_el in  w]
        if False not in result:
            print("You have Won!!!!!!!!!")
            display_board(board)
            return True
    return False
        
def choose_first():
    player=random.randint(1,2)
    return player

def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True

def full_board_check(board):
   for element in board:
        if element not in ['X','O']:
            return False
   return True

def player_choice(board):
    position=int(player_position())
    if not full_board_check(board):
        
        check=space_check(board,position-1) 
        while not check:
            position=input("Postion not empty. Give another position: ")
            position=int(position)
            check=space_check(board,position-1)
    else :
        print("Board is full")
        return False
    return position

def replay():
    play_again=input("Do you want to play again y/n: ")
    if play_again.lower() == 'y':
        
        return True
    else:
        return False
    

print('Welcome to Tic Tac Toe!\n\n\n')
play_again = True
test_board = ['','','','','','','','','','']
player=choose_first()
if player==1:
     p1="Player 1"
     p2="Player 2"
else:
    p1="Player 2"
    p2="Player 1"
print("{} goes first......".format(p1))
p1_marker=player_input()
if p1_marker == 'X':
    p2_marker = 'O'
else:
    p2_marker = 'X'
while play_again:
    
    display_board(test_board)
    
    
    print('\n'+p1)
    
    pos1=player_choice(test_board)
    test_board=place_marker(test_board,p1_marker,pos1)
    p1_winner=win_check(test_board,p1_marker)
    if p1_winner:
        test_board = ['','','','','','','','','','']
        play_again=replay()
        continue
    print('\n'+p2)
    pos2=player_choice(test_board)
    test_board=place_marker(test_board,p2_marker,pos2)
    p2_winner=win_check(test_board,p2_marker)
    if p2_winner:
        test_board = ['','','','','','','','','','']
        play_again=replay()
        continue
    if full_board_check(test_board):
        test_board = ['','','','','','','','','','']
        play_again=replay()
        
    
    
    
    
    
    
