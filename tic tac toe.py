#tic tac toe
from random import choice

def show_empity_board():
    board=[['1','2','3'],['4','5','6'],['7','8','9']]
    for row in board:
        for col in row:
            print(col, end='\t')
        print('\n')
    return board
    
def show_board(board):
    for row in board:
        for col in row:
            print(col, end='\t')
        print('\n')
        board[0][0]
    
def set_player_randomly():
    a=choice(['x','o'])
    if(a=='x'):
        b='o'
    else:
        b='x'        
    print(f'player 1 is: {a}')
    print(f'player 2 is: {b}')
    return (a,b)  

def input_from_user( board ,player ):
    while True:  
      player_input = input("please enter any number from 1 to 9 represents an empty position:  ")
      if player_input=='1' and board[0][0].isdigit() :
        board[0][0]=player
        break
      elif player_input=='2' and board[0][1].isdigit():
        board[0][1]=player
        break
      if player_input=='3' and board[0][2].isdigit():
        board[0][2]=player
        break
      if player_input=='4' and board[1][0].isdigit():
        board[1][0]=player
        break
      if player_input=='5' and board[1][1].isdigit():
        board[1][1]=player
        break
      if player_input=='6' and board[1][2].isdigit():
        board[1][2]=player
        break
      if player_input=='7' and board[2][0].isdigit():
        board[2][0]=player
        break
      if player_input=='8' and board[2][1].isdigit():
        board[2][1]=player
        break
      if player_input=='9' and board[2][2].isdigit():
        board[2][2]=player
        break
      else:
         print="invalid"
         continue
    show_board(board)

def check_full_board(board):
   for row in board:
      for col in row:
         if col.isdigit():
            return False
   return True      

def check_win(board):
   return board[0][0]==board[0][1]==board[0][2] or \
          board[1][0]==board[1][1]==board[1][2] or \
          board[2][0]==board[2][1]==board[2][2] or \
          board[0][1]==board[1][1]==board[2][1] or \
          board[0][0]==board[1][0]==board[2][0] or \
          board[0][2]==board[1][2]==board[2][2] or \
          board[0][0]==board[1][1]==board[2][2] or \
          board[0][2]==board[1][1]==board[2][2] 
  
def play():
  p1 , p2 = set_player_randomly()
  print("player1 : ",p1)
  print("player2 : ",p2)
  board = [['1','2','3'],['4','5','6'],['7','8','9']]
  show_board(board)
  while True:
     for player in [p1,p2]:
        print(f'{player} turn')
        input_from_user(board,player)
        if check_win(board):
           print(f'{player} wins')
           return
        if check_full_board(board):
           print('game finished. Draw!')
           return
      
play()                              