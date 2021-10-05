##Developing a Tic Tac Toe game.
## 1 create board and display board
##play game
  ## handle turn
import random 
game_still_going=True
current_player= "X"
valid=True

board=["-","-","-",
       "-","-","-",
       "-","-","-"]


def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8]+"\n")

    
def play_game():

    display_board()

    while game_still_going:
         handle_turn()

         switch_player()

         check_if_game_over()

         check_for_winner()

def play_gameAI():
    display_board()

    while game_still_going:
        handle_turnAI()
        
        switch_player()

        check_if_game_over()

        check_for_winner()

def handle_turn():
    global current_player
    global valid
    print(current_player+"'s turn")
    position = input("Pick a position by entering a whole number from 1 to 9: ")
    while position not in ['1','2','3','4','5','6','7','8','9']:
        print("That is an invalid input")
        position = input("Pick a position by entering a whole number from 1 to 9: ")
    position = int(position)-1
    
    if board[position]!="-":
            print("You can't go there!")
            valid=False
    
    if board[position] =="-":
        board[position]=current_player
        valid=True
         
    display_board()

def handle_turnAI():
    global current_player
    global valid
    print(current_player+"'s turn")
    if current_player == "O":
        if board[4]=="-":   # Starting position if there is no player move
            position = 5
        # Attacking 
        elif board[0]==board[1]=="O"and board[2]=="-":        # rows1
            position = 3
        elif board[1]==board[2]=="O"and board[0]=="-":        # rows1
            position = 1
        elif board[0]==board[2]=="O"and board[1]=="-":        # rows1
            position = 2
        elif board[3]==board[4]=="O" and board[5]=="-":     # rows2
            position = 6
        elif board[3]==board[5]=="O" and board[4]=="-":     # rows2
            position = 5
        elif board[5]==board[4]=="O" and board[3]=="-":     # rows2
            position = 4
        elif board[6]==board[7]=="O" and board[8]=="-":     # rows3
            position = 9
        elif board[8]==board[7]=="O" and board[6]=="-":     # rows3
            position = 7
        elif board[6]==board[8]=="O" and board[7]=="-":     # rows3
            position = 8
        elif board[0]==board[3]=="O" and board[6]=="-":     # columns1
            position = 7
        elif board[3]==board[6]=="O" and board[0]=="-":     # columns1
            position = 1
        elif board[0]==board[6]=="O" and board[3]=="-":     # columns1
            position = 4
        elif board[1]==board[4]=="O" and board[7]=="-":     # columns2
            position = 8
        elif board[4]==board[7]=="O" and board[1]=="-":     # columns2
            position = 2
        elif board[1]==board[7]=="O" and board[4]=="-":     # columns2
            position = 5
        elif board[2]==board[5]=="O" and board[8]=="-":     # columns3
            position = 9
        elif board[2]==board[8]=="O" and board[5]=="-":     # columns3
            position = 6
        elif board[8]==board[5]=="O" and board[2]=="-":     # columns3
            position = 3
        elif board[0]==board[4]=="O" and board[8]=="-":     # diagonal1
            position = 9
        elif board[0]==board[8]=="O" and board[4]=="-":     # diagonal1
            position = 5
        elif board[8]==board[4]=="O" and board[0]=="-":     # diagonal1
            position = 1
        elif board[2]==board[4]=="O" and board[6]=="-":     # diagonal2
            position = 7
        elif board[6]==board[4]=="O" and board[2]=="-":     # diagonal2
            position = 3
        elif board[2]==board[6]=="O" and board[4]=="-":     # diagonal2
            position = 5
            #block
        elif board[0]==board[1]!="-"and board[2]=="-":        # rows1
            position = 3
        elif board[1]==board[2]!="-"and board[0]=="-":        # rows1
            position = 1
        elif board[0]==board[2]!="-"and board[1]=="-":        # rows1
            position = 2
        elif board[3]==board[4]!="-" and board[5]=="-":     # rows2
            position = 6
        elif board[3]==board[5]!="-" and board[4]=="-":     # rows2
            position = 5
        elif board[5]==board[4]!="-" and board[3]=="-":     # rows2
            position = 4
        elif board[6]==board[7]!="-" and board[8]=="-":     # rows3
            position = 9
        elif board[8]==board[7]!="-" and board[6]=="-":     # rows3
            position = 7
        elif board[6]==board[8]!="-" and board[7]=="-":     # rows3
            position = 8
        elif board[0]==board[3]!="-" and board[6]=="-":     # columns1
            position = 7
        elif board[3]==board[6]!="-" and board[0]=="-":     # columns1
            position = 1
        elif board[0]==board[6]!="-" and board[3]=="-":     # columns1
            position = 4
        elif board[1]==board[4]!="-" and board[7]=="-":     # columns2
            position = 8
        elif board[4]==board[7]!="-" and board[1]=="-":     # columns2
            position = 2
        elif board[1]==board[7]!="-" and board[4]=="-":     # columns2
            position = 5
        elif board[2]==board[5]!="-" and board[8]=="-":     # columns3
            position = 9
        elif board[2]==board[8]!="-" and board[5]=="-":     # columns3
            position = 6
        elif board[8]==board[5]!="-" and board[2]=="-":     # columns3
            position = 3
        elif board[0]==board[4]!="-" and board[8]=="-":     # diagonal1
            position = 9
        elif board[0]==board[8]!="-" and board[4]=="-":     # diagonal1
            position = 5
        elif board[8]==board[4]!="-" and board[0]=="-":     # diagonal1
            position = 1
        elif board[2]==board[4]!="-" and board[6]=="-":     # diagonal2
            position = 7
        elif board[6]==board[4]!="-" and board[2]=="-":     # diagonal2
            position = 3
        elif board[2]==board[6]!="-" and board[4]=="-":     # diagonal2
            position = 5
        else:
            position = random.randint(1,9)
        
    else:
         position = input("Pick a position by entering a whole number from 1 to 9: ")
         while position not in ['1','2','3','4','5','6','7','8','9']:
            print("That is an invalid input")
            position = input("Pick a position by entering a whole number from 1 to 9: ")
    position = int(position)-1
    
    if board[position]!="-":
            print("\nYou can't go there!\n")
            valid=False
    
    if board[position] =="-":
        board[position]=current_player
        valid=True
    display_board()

def switch_player():
    global current_player
    global valid
    if current_player == "X" and valid:
        current_player = "O"
    elif current_player =="O" and valid:
        current_player="X"

def check_if_game_over():
    global Tie
    global game_still_going
    global current_player
    if "-" not in board or check_for_winner() != None:
        game_still_going = False
        winner=check_for_winner()
        try:
            print(winner+ " won, GAME OVER")
        except:
            print("Tie")


def check_for_winner():
    ##check_rows
    if board[0]==board[1]==board[2] != "-":
        return board[1]
    elif board[3]==board[4]==board[5] != "-":
        return board[4]
    elif board[6]==board[7]==board[8] != "-":
        return board[7]
        
    ##check_columns
    if board[0]==board[3]==board[6] != "-":
        return board[3]
    elif board[1]==board[4]==board[7] != "-":
        return board[4]
    elif board[2]==board[5]==board[8] != "-":
        return board[5]
    ##check_diagonals
    if board[0]==board[4]==board[8] != "-":
        return board[4]
    elif board[2]==board[4]==board[6] != "-":
        return board[4]


def play_again():
    t=True
    global game_still_going
    global board
    board=["-","-","-","-","-","-","-","-","-"]
    game_still_going=True
    while t:
        answer = input("\nDo you want a Replay?\n Yes(1) or No(2): ")
        if answer == str(1):
            pick_mode()
            break
        elif answer == str(2):
            print("\nOkay, Sad To See You Go\nGood Bye! 😭")
            break
        else:
            print("\nThat was an invalid input!")

def pick_mode():
    while True:
        global no_of_players
        no_of_players = input("\n\n**************************************************************************************\n\nHUMAN vs AI(1)\nHUMAN vs HUMAN(2)\n\nselect 1 or 2: ")
        if no_of_players == str(2):
            play_game()
            break
        elif no_of_players == str(1):
            play_gameAI()
            break
        else:
            print("\nThat was an invalid input!")
        
        
pick_mode()

while game_still_going == False:
    play_again()

