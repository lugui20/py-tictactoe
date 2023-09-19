from random import randrange

board = [[1,2,3],[4,5,6],[7,8,9]]
player_is_next = False
player_won = False
computer_won = False

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[0][0]) + "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[1][0]) + "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[2][0]) + "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        while True:
            try:
                user_move = int(input("Enter your move: "))
                break
            except:
                print("Invalid input, please try again.")
        if user_move < 1 or user_move > 9:
            print("The position must be in range from 1 to 9")
        else:
            user_move_elem = position_to_elem(user_move)
            if user_move_elem in make_list_of_free_fields(board):
                board[user_move_elem[0]][user_move_elem[1]] = "O"
                break
            else:
                print("This position is used. Please, select another:")
    #display_board(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                free_fields += ((i,j)),
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    counter = 0

    #Check rows
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                counter += 1
        if counter == 3:
            return True
        counter = 0
    
    #Check lines
    for j in range(3):
        for i in range(3):
            if board[i][j] == sign:
                counter += 1
        if counter == 3:
            return True
        counter = 0
    
    #Check main diagonal
    for m in range(3):
        if board[m][m] == sign:
            counter += 1
    if counter == 3:
        return True
 
    counter = 0   
    #Check antidiagonal
    for a in range(3):
        if board[2-a][a] == sign:
            counter += 1
    if counter == 3:
        return True
    
    return False

def computer_move(board):
    # The function draws the computer's move and updates the board. 
    while True:
        computer_move = randrange(9) + 1
        computer_move_elem = position_to_elem(computer_move)
        if computer_move_elem in make_list_of_free_fields(board):
            board[computer_move_elem[0]][computer_move_elem[1]] = "X"
            break
        else:
            continue

def position_to_elem(number):

    if number < 4: row = 0
    elif number > 6: row = 2
    else: row = 1

    if number % 3 == 0: column = 2
    elif number % 3 == 2: column = 1
    else: column = 0

    elem = (row, column)

    return elem

while len(make_list_of_free_fields(board)) != 0:
    if player_is_next == True:
        display_board(board)
        enter_move(board)
        if victory_for(board, "O"):
            player_won = True
            break
        player_is_next = False
    else:
        computer_move(board)
        if victory_for(board, "X"):
            computer_won = True
            break
        player_is_next = True

display_board(board)
if player_won == True:
    print("You won!")
elif computer_won == True:
    print("You lost!")
else:
    print("Tie!")
