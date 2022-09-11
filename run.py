
board = []

def welcome():
    """
    A function to welcome the user to the game and tell the rules.
    It also takes the users name and ask if the user is ready. 
    """

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
    return player_name


def get_player_name():
    """
    A function to get the players name and validate that it is only letters used. 
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

        start_answer = input("Ready to start press y for yes, n for no: ").lower()

        if start_answer == "y":
            print("\nGame is starting")
            break
        elif start_answer == "n":
            print("\nThats to bad, hope you will have a have a nice day")
            break
        else:
            print("\nYou need to answer with a y or n\n")

def create_the_board():
    """
    A function to create the gameboard. At the moment it will create a 3X3 squareboard.
    """
    global board
    size = 3
    for i in range(size):
        row = []
        for j in range(size):
            row.append("[]")
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
def make_move(board,row,col,player):
    """
    A function to put a move in to the board
    """
    board[row][col]= player

# welcome()
# ready_to_start()
create_the_board()
show_board(board)
make_move(board, 1, 1, "X")
show_board(board)
make_move(board, 0, 1, "O")
show_board(board)