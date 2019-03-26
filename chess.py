###
### Author: Pearce Phanawong
### Description: This program runs a game of 1D chess. It involves
###              each player having 2 knights that can move two
###              spaces in either direction and a king that moves
###              until it reaches another piece or an end of the
###              board. The game is played on a 1x9 board takes
###              user input for which piece to be moved and which
###              direction to move it.
###

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'

def is_valid_move(board, position, player):
    '''
    This function checks if the player's move will be a valid one
    based on whether it is the player's piece and if it's in the
    correct spot.
    '''
    if position <= 8 and position >= 0:
        if player == WHITE:
            if board[position] == W_KNIGHT or board[position] == W_KING:
                return True
            return False
        else:
            if board[position] == B_KNIGHT or board[position] == B_KING:
                return True
            return False

def move_knight(board, position, direction):
    '''
    This function will move the knight piece two spaces in either
    direction and will replace whatever piece or spot it lands
    on. The space it was previously at will become an empty space.
    '''
    if direction == LEFT:
        if position >= 2:
            board[position - 2] = board[position]
            board[position] = EMPTY
    if direction == RIGHT:
        if position <= 6:
            board[position + 2] = board[position]
            board[position] = EMPTY


def move_king(board, position, direction):
    '''
    This function will move the king piece in one direction until
    it either hits another piece or reaches the end of one side of
    the board. It will replace whatever piece or spot it lands
    on. The space it was previously at will become an empty space.
    '''
    if direction == LEFT:
        i = 0
        king = board[position]
        board[position] = EMPTY
        while i == 0:
            if position != 0:
                position -= 1
                if board[position] != EMPTY:
                    board[position] = king
                    i += 1
            else:
                i += 1
                board[position] = king
    if direction == RIGHT:
        i = 0
        king = board[position]
        board[position] = EMPTY
        while i == 0:
            if position != 8:
                position += 1
                if board[position] != EMPTY:
                    board[position] = king
                    i += 1
            else:
                i += 1
                board[position] = king


def print_board(board):
    '''
    This function will print out a "board" with the location
    of all the pieces still in the game
    '''
    print('+-----------------------------------------------------+')
    for i in range(len(board)):
        print('| ' + board[i] + ' ', end = '')
    print('|')
    print('+-----------------------------------------------------+')

def draw_board(board, gui):
    '''
    This function will create a graphical image of the board while
    the game is played.
    '''



def is_game_over(board):
    '''
    This function checks if the white or black king is still
    on the board, and if it is not, will print whether the white
    player or black player won.
    '''
    if W_KING in board and B_KING in board:
        return False
    elif B_KING in board and not W_KING in board:
        print_board(board)
        print('Black wins!')
        return True
    else:
        print_board(board)
        print('White wins!')
        return True


def move(board, position, direction):
    '''
    This function checks whether the piece is a king or knight
    and then will call the appropriate function to move the
    piece.
    '''
    if board[position] == W_KNIGHT or board[position] == B_KNIGHT:
        move_knight(board, position, direction)
    else:
        move_king(board, position, direction)


def main():

    # Create the canvas
    #gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        #draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            is_game_won = is_game_over(board)

main()