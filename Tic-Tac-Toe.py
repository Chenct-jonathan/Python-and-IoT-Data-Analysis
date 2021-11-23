import random
board=['1','2','3','4','X','6','7','8','9']

def display_board(board):
    print ('+---|---|---+')
    print ('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')
    print ('|   |   |   |')
    print ('+-----------+')
    print ('|   |   |   |')
    print ('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ' )
    print ('|   |   |   |')
    print ('+-----------+') 
    print ('|   |   |   |')
    print ('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print ('+---|---|---+')
    
    
def enter_move(board): 
    free = make_list_of_free_fields(board)
    playermove=int(input("Your move:"))
    board[playermove-1]='O'
            
    
    
def make_list_of_free_fields(board):
    free = []
    for i in range(9):
        if (board[i] in "012345678"): free.append(i)
    return free

def draw_move(board):
    free = make_list_of_free_fields(board)
    board[free[random.randint(0,len(free)-1)]]='X'
    
def victory_for(board):
    for i in range (0,3,3):
        if (board[i] == board[i+1] == board[i+2]):return True
    for i in range (0,3):
        if (board[i] == board[i+3] == board[i+6]):return True 
    if (board[0] == board[4] == board[8]): return True
    if (board[2] == board[4] == board[6]): return True
        


switch = 1
while (switch<9):
    display_board(board)
    if (switch%2 == 1):
        enter_move(board)
        display_board(board)
    else: draw_move(board)
    display_board(board)
    switch += 1
    if (victory_for(board)):
        if (switch%2 == 1):print("You Lost!")
        else: print("You Won!")
        break
    
else:
    print("Draw")


print("Game Over")




