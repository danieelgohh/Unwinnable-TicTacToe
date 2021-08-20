import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    
    # next move in a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        spot = random.choice(game.available_moves())
        return spot

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_spot = False
        val = None
        while not valid_spot:
            spot = input(self.letter + '\'s turn. Select your next move (0-8): ')
            # value checker to see if value is correct by trying to cast it to 
            # an integer, if not possible, notify that it is invalid and also check
            # if spot is available.
            try: 
                val = int(spot)
                if val not in game.available_moves():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print('Invalid spot!')

        return val

class UnbeatableComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            spot = random.choice(game.available_moves()) # random spot on grid
        else:
            # get the spot based on the minimax algorithm
            spot = self.minimax(game, self.letter)['position']
        return spot
    
    def minimax(self, state, player):
        max_player = self.letter # UnbeatableComputerPlayer
        other_player = 'O' if player == 'X' else 'X' # the other player

        # firstly check if previous move won 
        # base case
        if state.current_winner == other_player:
            # return position and score to keep track of the score 
            return  {'position': None,
                    'score': 1 * (state.num_empty_spots() + 1) if other_player == max_player else 
                    -1 * (state.num_empty_spots() + 1)
                    }
        elif not state.empty_spots(): # no empty spots on grid
            return {'position': None, 'score': 0} 

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize
        
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move
            simulate_score = self.minimax(state, other_player) # alternate players
            
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            simulate_score['position'] = possible_move # otherwise this will be messed up from the recursion

            # step 4: update the dictionaties if necessary
            print(player)
            print(simulate_score)
            print(best)
            if player == max_player:
                if simulate_score['score'] > best['score']:
                    best = simulate_score # replace best
            else: 
                if simulate_score['score'] < best['score']:
                    best = simulate_score # replace best


        return best



