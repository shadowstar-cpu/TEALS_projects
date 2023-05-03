EMPTY = "   "
X =     " X "
O =     " O "
reset = 'y'
player = X

def initialize():
    global board, winner, player, i
    pick_player = input('Who would you like to go first? X or O\n')
    if pick_player == 'X':
        player = X
    if pick_player == 'O':
        player = O
    board = [
        None,  # board[0] is not used.
        EMPTY, EMPTY, EMPTY,
        EMPTY, EMPTY, EMPTY,
        EMPTY, EMPTY, EMPTY,
    ]
    winner = None
    i = 1

def show_chart():
    print(
        " 1 | 2 | 3 ",
        "-----------",
        " 4 | 5 | 6 ",
        "-----------",
        " 7 | 8 | 9 ",
        sep="\n",
    )


def show_board():
    print(board[1], board[2], board[3], sep="|")
    print("-----------")
    print(board[4], board[5], board[6], sep="|")
    print("-----------")
    print(board[7], board[8], board[9], sep="|")

def announce_winner():
    global reset
    if winner == None:
        print("It is a tie!")
        reset = input('would you like to play again? respond with lowercase y for yes or lowercase n for no.\n')
    elif winner == X:
        print("Player X is the winner!")
        reset = input('would you like to play again? respond with lowercase y for yes or lowercase n for no.\n')
    else:
        print("Player O is the winner!")
        reset = input('would you like to play again? respond with lowercase y for yes or lowercase n for no.\n')


def make_a_move(player):
    move = int(input('Player' + player + 'your move?\n'))
    if 1 <= move and move <= 9 and board[move] == EMPTY:
        board[move] = player
    else:
        print("Not a legal move.")
        show_chart()
        print()
        show_board()
        make_a_move(player)


def take_a_turn(player):
    global winner

    if winner != None:   # Stop when someone wins.
        return

    make_a_move(player)
    show_board()
    if check_for_winner():
        winner = player


def check_for_winner():
    return check_across() or check_down() or check_diagonal()


def check_across():
    return check(1, 2, 3) or check(4, 5, 6) or check(7, 8, 9)


def check_down():
    return check(1, 4, 7) or check(2, 5, 8) or check(3, 6, 9)


def check_diagonal():
    return check(1, 5, 9) or check(3, 5, 7)


def check(first_space, second_space, third_space):
    return (
        board[first_space] != EMPTY
        and board[first_space] == board[second_space]
        and board[first_space] == board[third_space]
    )


def play_a_game():
    """ Play a game of Tic-Tac-Toe. For 2 players. Uses the console. """
    initialize()
    global i, player
    print("Use this chart to select your next move:")
    show_chart()
    while i < 9:
        take_a_turn(player)  # 9 turns max in a game
        i = i + 1
        if player == X:
            player = O
        else:
            player = X
    announce_winner()

while reset == 'y':
    play_a_game()
print('Have a nice day!')