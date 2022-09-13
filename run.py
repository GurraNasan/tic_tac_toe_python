import random

board = []
player = "X"
win = None
player_name = None


def welcome():
    """
    A function to welcome the user to the game and tell the rules.
    It also takes the users name and ask if the user is ready. 
    """

    global player_name
    print("")
    print("####################################")
    print("# Welcome to a game of TIC TAC TOE #")
    print("####################################\n")
    player_name = get_player_name()

    print(f"\nOk, {player_name} the rules for this game is:")
    print(
        '''
        The goal is to get a sequence from one side of the board to the other.
        You will take turns with the computer. 
        You can get a sequence horizontally, vertical or diagonally. 
        If the board is full without anyone made a sequence it will be a tie  
        ''')
    

def get_player_name():
    """
    A function to get the players name and 
    validate that it is only letters used. 
    """

    while True:
        name = input("What is you name?: ").capitalize()

        if name.isalpha():
            return name
        else:
            print("You can only use letters, please try again")


def ready_to_start():
    """
    A function to check if the user is ready to start the game
    """
    while True:

        start_answer = input("Start new game press y or n: ").lower()

        if start_answer == "y":
            print("\nGame is starting")
            main(player_name)
            break
        elif start_answer == "n":
            print("\nThats to bad, hope you will have a have a nice day")
            break
        else:
            print("\nYou need to answer with a y or n\n")


def create_the_board():
    """
    A function to create the gameboard.
    At the moment it will create a 3X3 squareboard.
    """

    global board
    board = []
    size = 3
    for i in range(size):
        row = []
        for j in range(size):
            row.append("_")
        board.append(row)
    return board


def show_board(board):
    """
    Function to show the board for the user
    """

    for row in board:
        for item in row:
            print(item, end=" ")
        print()
    print("")
    print("")


def make_move(board, row, col, player):
    """
    A function to put a move in to the board
    """

    board[row][col] = player
    

def users_move(board, user):
    """
    A function to take the users move and check if it is valid or not
    """

    while True:
        try: 
            row, col = list(map(int, input(
                "Enter row and column as (1,1): "
                ).split(",")))
            row = row - 1
            col = col - 1
            if row >= 3 or col >= 3 or row <= -1 or col <= -1:
                print(
                    "\nYou put your move outside the board\n"
                    )
            elif board[row][col] != "_":
                print("\nSpot taken, make a new one\n")
            else:
                break
        except ValueError:
            print("\nThat is not a valid move\n")  

    make_move(board, row, col, user)


def check_if_winner(board, player):
    """
    A function to check if the current player is the winner.
    """

    num = len(board)
    global win
   
    # Check rows
    for i in range(num): 
        win = True  
        for j in range(num):
            if board[i][j] != player.upper():
                win = False
                break
        if win:
            return win        

    # Check collumns
    for i in range(num):
        win = True
        for j in range(num):
            if board[j][i] != player.upper():
                win = False
                break
        if win:
            return win         

    # Check diagonals
    for i in range(num):
        win = True
        if board[i][i] != player.upper():
            win = False
            break
    if win:
        return win      

    for i in range(num):
        win = True
        if board[i][i - 1 - i] != player.upper():
            win = False
            break
    if win:
        return win 
    return win


def check_draw(board):
    """ 
    A function to check if the game is draw. 
    """

    for row in board:
        for item in row:
            if item == "_":
                return False
    return True


def change_player():
    """
    A function to change the player
    """
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def computer_move():
    """
    function to make the computer do a random move
    """

    while player == "O":
        row_num = random.randint(0, 2)
        col_num = random.randint(0, 2)
        if board[row_num][col_num] == "_":
            make_move(board, row_num, col_num, player)
            
            if check_if_winner(board, player):
                print("\nSorry you lost!!\n")
                return True
            change_player()
            

def main(name):
    """
    A function to run the game
    """

    create_the_board()
    while True:
        show_board(board)
        users_move(board, player)
        
        if check_if_winner(board, player):
            print(f"\n{name} you won!!\n")
            break

        if check_draw(board):
            print("\nThe game was draw\n")
            break

        print("\nThe board:")
        change_player()
        if computer_move():
            break

    show_board(board)
    ready_to_start()

welcome()
ready_to_start()
