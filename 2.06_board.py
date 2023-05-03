#Nickelson, Ronald
#2/27/23
#Intro to CS
board = list((
"1", "2", "3",
"4", "5", "6",
"7", "8", "9",))

print(' {}|{}|{}'.format(board[0], board[1], board[2]))
print('-------')
print(' {}|{}|{}'.format(board[3], board[4], board[5]))
print('-------')
print(' {}|{}|{}'.format(board[6], board[7], board[8]))
player_move = input('what number on the board would you like to mark? ')
int_player_move = (int(player_move)-1)
board[0] = ' '
board[1] = ' '
board[2] = ' '
board[3] = ' '
board[4] = ' '
board[5] = ' '
board[6] = ' '
board[7] = ' '
board[8] = ' '
board[int_player_move] = 'X'
print('your move is ' + player_move)
print(' {}|{}|{}'.format(board[0], board[1], board[2]))
print('-------')
print(' {}|{}|{}'.format(board[3], board[4], board[5]))
print('-------')
print(' {}|{}|{}'.format(board[6], board[7], board[8]))