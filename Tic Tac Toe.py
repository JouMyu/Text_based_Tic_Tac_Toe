#This is a project that allows 2 players to play tic-tac-toe in a text based game

"""
DECLARING ESSENTIAL VARIABLES
"""
#Variable to determine whether game is running
game_running = True
#Variable to determine whether symbol selection is running
symbol_selection = True
#Variable to determine whether turns are being taken
turn_taking = True
#List of player symbols available for the game
initial_player_symbols = ['', '']
#Initial turn count
turn_counter = 0

'''
DECLARING ESSENTIAL GAME FUNCTIONS
'''


#Generates an empty board ready for a new game
def initial_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board


#Function displays the board in its current state
def display_board(board):
    print('-|-----|-----|-----|-')
    print(f' |  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |')
    print('-|-----|-----|-----|-')
    print(f' |  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |')
    print('-|-----|-----|-----|-')
    print(f' |  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |')
    print('-|-----|-----|-----|-')


#Function that allows player to choose name
def choose_name():
    player1_name = input('Player 1 name: ')
    player2_name = input('Player 2 name: ')
    return player1_name, player2_name


#Function that takes player input so that player can choose the symbol they want to use
def choose_symbol(player_symbols, player_names):
    print('Players, you can now choose your symbols!')
    while True:
        player1_symbol = input(f'{player_names[0]}, choose a symbol: ')
        player2_symbol = input(f'{player_names[1]}, choose a symbol: ')
        if player1_symbol == player2_symbol:
            print(f'Do not choose the same symbols!')
        elif len(player1_symbol) > 1 or len(player2_symbol) > 1:
            print(f'Make sure your symbol is only 1 character long!')
        else:
            break

        #OLD CODE WHERE ONLY X OR O CAN BE USED AS SYMBOLS
        '''
        if player1_symbol == 'X':
            player2_symbol = 'O'
            print(f'{player_names[1]}, your symbol is O')
            break
        elif player1_symbol == 'O':
            player2_symbol = 'X'
            print(f'{player_names[1]}, your symbol is X')
            break
        else:
            print('Invalid symbol, please try again.')
        '''

    player_symbols[0] = player1_symbol
    player_symbols[1] = player2_symbol
    return player_symbols


#Function takes player input and returns the updated board values

def player_input(symbol, board, player_name):
    values = [0, 1, 2]
    while True:
        try:
            player_turn_row = int(input(f'{player_name}, please enter the row of your turn, either 1, 2, or 3: ')) - 1
        except:
            print('Please enter a valid number.')
            continue

        try:
            player_turn_column = int(
                input(f'{player_name}, please enter the column of your turn, either 1, 2, or 3: ')) - 1
        except:
            print('Please enter a valid number.')
            continue

        if player_turn_row not in values and player_turn_column not in values:
            print('Invalid row and column, please try again.')
        elif player_turn_row not in values:
            print('Invalid row, please try again.')
        elif player_turn_column not in values:
            print('Invalid column, please try again.')
        elif board[player_turn_row][player_turn_column] != ' ':
            print('This cell is already occupied, please try again.')
        else:
            break

    board[player_turn_row][player_turn_column] = symbol
    return board


#Function checks the current state of the board and declares whether a win has been met
def check_win(board):
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != ' ':
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != ' ':
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != ' ':
        return True
    elif board[0][0] == board[0][1] == board[0][2] and board[0][0] != ' ':
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != ' ':
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != ' ':
        return True
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    else:
        return False


#Function checks whether the board is full
def full_board_check(board):
    for row in board:
        for column in row:
            if column == ' ':
                return False
    return True


#Function asks whether player wishes to play again
def play_again():
    while True:
        replay_question = input('Do you want to play again? (y/n): ')
        if replay_question == 'y':
            return True
        elif replay_question == 'n':
            return False
        else:
            print('Invalid input, please try again.')


#MAIN GAME LOOP-------------------------------------------------------------------

#Prints welcome message
print('WELCOME TO TIC TAC TOE!')

while game_running:
    while symbol_selection:
        chosen_names = choose_name()
        chosen_symbols = choose_symbol(initial_player_symbols, chosen_names)
        symbol_selection = False
    print('Here is the initial board:')
    game_board = initial_board()
    display_board(initial_board())
    while turn_taking:
        if turn_counter % 2 == 0:
            players_turn = chosen_symbols[0]
            current_player = chosen_names[0]
        elif turn_counter % 2 == 1:
            players_turn = chosen_symbols[1]
            current_player = chosen_names[1]

        board_after_turn = player_input(players_turn, game_board, current_player)
        print('Here is the board after your turn:')
        display_board(board_after_turn)
        if check_win(board_after_turn):
            print(f'Congratulations Player {current_player}! You win after {turn_counter} turns!')
            turn_taking = False
        elif full_board_check(board_after_turn):
            print('The board is full! The game is a draw!')
            turn_taking = False
        else:
            turn_counter += 1

    replay = play_again()
    if replay:
        symbol_selection = True
        turn_taking = True
    else:
        symbol_selection = False
        turn_taking = False
        game_running = False
