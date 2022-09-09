
player_name = none

def welcome():
    """
    A function to welcome the user to the game and tell the rules.
    It also takes the users name and ask if the user is ready. 
    """

    print("")
    print("####################################")
    print("# Welcome to a game of TIC TAC TOE #")
    print("####################################\n")
    player_name = input("What is your name?: ")

    print(f"\nOk, {player_name} the rules for this game is:")
    print(
    '''
    The goal is to get a sequence from one side of the board to the other.
    You will take turns with the computer. 
    You can get a sequence horizontally, vertical or diagonally. 
    If the board is full without anyone made a sequence it will be a tie  
    ''')
    start_answer = input("Ready to start press y for yes, y for no: ")
    

    


welcome()