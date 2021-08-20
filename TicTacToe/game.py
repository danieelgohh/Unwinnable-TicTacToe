import time
import math
from player import HumanPlayer, RandomComputerPlayer, UnbeatableComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # single list to represent 3x3 board
        self.current_winner = None # track winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to which box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x' , 'x' , 'o'] => [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_spots(self):
        return ' ' in self.board

    def num_empty_spots(self):
        return self.board.count(' ')
        # or
        # return len(self.available_moves())

    def make_move(self, spot, letter):
        # if valid move, then make the move (assign letter to grid spot)
        #then return true, if not, return false
        if self.board[spot] == ' ':
            self.board[spot] = letter
            if self.winner(spot, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, spot, letter):
        # winner if 3 in a row, diagonally or straight 
        # check row
        row_ind = spot // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([grid == letter for grid in row]):
            return True

        # check column
        col_ind = spot % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([grid == letter for grid in column]):
            return True

        # check diagonals 
        # only possible if spot is even number (0, 2, 4, 6, 8)
        if spot % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([grid == letter for grid in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([grid == letter for grid in diagonal2]):
                return True

        # if all of the above does not match
        return False

def play(game, x_player, o_player, print_game=True):
    # returns results of the game
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter
    # iterate if the game still has empty squares or break the loop and 
    # announce the winner 
    while game.empty_spots():
        if letter == 'O':
            spot = o_player.get_move(game)
        else:
            spot = x_player.get_move(game)
    
        if game.make_move(spot, letter):
            if print_game:
                print(letter + f' makes a move to spot {spot}')
                game.print_board()
                print('')

        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter


        # alternate the letters
        letter = 'O' if letter == 'X' else 'X'

    # tiny break to look like the computer is thinking of a move
    time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = UnbeatableComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)