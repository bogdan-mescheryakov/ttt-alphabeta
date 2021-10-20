class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

    
        self.player_turn = 'X'

    def greeting(self):
        self.player = 'x'
        hi = input("\t What do you prefer X or O ?\n")

        if hi == 'X' or hi == 'x':
            self.ai_player = 'o'
        elif hi == 'O' or hi == 'o' or hi == '0':
            self.player = 'o'
            self.ai_player = 'x'
        else:
            print("XXXXX    You have to choose X or O to play this game. OOOOO\n")
            self.greeting()
    
    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('|{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def draw_reference_board(self):   # to provide convenient reference for user
        numbers = (x for x in range(1,10))
        for i in range(3):
            for j in range(3):
                print("|{}|".format(next(numbers)), end=" ")
            print()
        print()
    
    def first_move_notice(self):
        good_luck = ("""
        XXX    To make your first move, press a correspondent number from 1 to 9.   OOO 
                                And then hit Enter.Good luck! 
        """)
        print(good_luck)

    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    def digit(self): # easier input for the move
        button = input("Your move:")
            
        if button == "1":
            return 0, 0
        elif button == "2":
            return 0, 1
        elif button == "3":
            return 0, 2
        elif button == "4":
            return 1, 0
        elif button == "5":
            return 1, 1
        elif button == "6":
            return 1, 2
        elif button == "7":
            return 2, 0
        elif button == "8":
            return 2, 1
        elif button == "9":
            return 2, 2

    def is_end(self):
    # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # First diagonal win
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        
        for i in range(0, 3):
            for j in range(0, 3):
                # we continue the game
                if (self.current_state[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'

    def max_alpha_beta(self, alpha, beta):
        maxv = -2
        px = None
        py = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'
                    
                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv

        return (maxv, px, py)

    def min_alpha_beta(self, alpha, beta):

        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)

    def play_alpha_beta(self):
        self.greeting()
        self.first_move_notice()
        while True:
            self.draw_reference_board()
            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It's a tie!")


                self.initialize_game()
                return

            if self.player == 'x':
                if self.player_turn == 'X':

                    while True:
                        px, py = self.digit()

                        if self.is_valid(px, py):
                            self.current_state[px][py] = 'X'
                            self.player_turn = 'O'
                            break
                        else:
                            print('It\'s not a valid move, choose an available slot from 1 to 9, please.')

                else:
                    (m, px, py) = self.max_alpha_beta(-2, 2)
                    self.current_state[px][py] = 'O'
                    self.player_turn = 'X'
            
            if self.player == 'o':
                if self.player_turn == 'X':

                    while True:
                                              
                        (m, px, py) = self.max_alpha_beta(-2, 2)
                        
                        if self.is_valid(px, py):
                            self.current_state[px][py] = 'X'
                            self.player_turn = 'O'
                            break
                        else:
                            print('It\'s not a valid move, choose an available slot from 1 to 9, please.')
                
                else:
                    px, py = self.digit()
                    
                    if self.is_valid(px, py):
                            self.current_state[px][py] = 'O'
                            self.player_turn = 'X'
 
def main():
    g = Game()
    g.play_alpha_beta()

if __name__ == "__main__":
    main()