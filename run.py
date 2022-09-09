

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
    start_answer = input("Ready to start press y for yes, y for no: ")
    
def get_player_name():
    """
    A function to get the players name and validate that it is only letters used. 
    """
    name = input("What is you name?: ").capitalize()
    while True:
        if name.isalpha():
            return name
        else:
            print("You can only use letters")

welcome()