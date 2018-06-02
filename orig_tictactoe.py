#!/usr/bin/python3
#
# Wesleyan University
# COMP 332, Spring 2018
# Homework 1: Tic-tac-toe game

# Nikhil Ghosh

import random

class Board():
    """
    TicTacToe game board

    Player is "X", and goes first. Server is "0", and goes second.
    """

    def __init__(self, n):
        self.n = n
## This class is not used ##

class TicTacToe():

    """
    TicTacToe game
    """

    def __init__(self, n):
        self.n = n
        self.board = [([(" - ") for i in range(self.n)]) for j in range(self.n)]
        self.moves = 0
        self.max_moves = n*n

    def display(self):
        for row in self.board:
            print(''.join(str(thing) for thing in row))
        print("")
    
    def board_full(self):
        return self.moves == self.max_moves

    def game_won(self):
        # Horizontals (n possible)
        for row in self.board:
            if all(x == " X " for x in row) or all(x == " O " for x in row):
                return True
        
        # Verticals (n possible)
        for i in range(self.n):
            # Create temp list for all vals @ each position
            temp = [row[i] for row in self.board]
            if all(x == " X " for x in temp) or all(x == " O " for x in temp):
                return True
       
       # Diagonals (2 possible)
            # top left -> bottom right
        temp = []
        for i in range(self.n):
            temp.append(self.board[i][i])
        if all(x == " X " for x in temp) or all(x == " O " for x in temp):
                return True
            
            # top right -> bottom left
        temp = []
        i = self.n - 1
        while i >= 0:
            temp.append(self.board[self.n - i - 1][i])
            i -= 1
        if all(x == " X " for x in temp) or all(x == " O " for x in temp):
                return True
        return False

    def make_move(self, letter, r, c):
        # Takes letter, row, column
        # Put move onto the board
        self.board[r][c] = letter
        # display board
        self.display()
        # increment count of moves
        self.moves += 1

    def is_taken(self, r, c):
        return self.board[r][c] != " - "


class Server():
    """
    Server for TicTacToe game
    """

    def __init__(self):
        print('')

    def play(self):

        print("==================")
        print("| TicTacToe Game |")
        print("|  Nikhil Ghosh  |")
        print("|   COMP 332     |")
        print("==================\n")

        board_size = int(input("Enter number of rows in TicTacToe board: "))
        t = TicTacToe(board_size)
        t.display()

        # Play the game until it's won or tied (full)
        while (not t.game_won()) and (not t.board_full()) :
            ##############################           
            ##############################
            #######   Player Move  #######
            ##############################
            ##############################

            # Prompt player for row and column
            idx = board_size - 1
            (p_row, p_col) = (board_size + 1, board_size + 1)
            while p_row >= board_size or p_row < 0:
                p_row = int(input("Choose row: [0 - %d]: " % (idx)))
            while p_col >= board_size or p_col < 0:
                p_col = int(input("Choose col: [0 - %d]: " % (idx)))

            # Catch if it's already taken
            while t.is_taken(p_row, p_col):
                (p_row, p_col) = (board_size + 1, board_size + 1)
                while p_row >= board_size or p_row < 0:
                    p_row = int(input("Choose row: [0 - %d]: " % (idx)))
                while p_col >= board_size or p_col < 0:
                    p_col = int(input("Choose col: [0 - %d]: " % (idx)))

            # Execute player move, check status
            print("")
            print("Player move: ")
            t.make_move(" X ", p_row, p_col)
            if t.game_won():
                print("Player wins!")
                break
            elif t.board_full():
                print("Tie game!")
                break

            ##############################
            ##############################
            # Opportunistic Server move #
            ##############################
            ##############################

            ## HORIZONTAL winning move available?
            # for row in t.board:
            #     if row.count(" O ") == board_size - 1 and row.count(" - ") == 1:
            #         s_row = t.board.index(row) # position of row on board
            #         s_col = row.index(" - ") # position of blank in row
            #     else:
            #         ## VERTICAL winning move available?
            #         for i in range(t.n):
            #             # Create temp list for all vals @ each position
            #             temp = [row[i] for row in t.board]
            #             if temp.count(" O ") == board_size - 1 and temp.count(" - ") == 1:
            #                 s_row = temp.index(" - ") # position of blank in row
            #                 s_col = i # ith column
            #             else:
            #                 ## DIAGONAL winning move available? Note; all moves of form (n, n)
            #                 ## top left -> bottom right diagonal
            #                 temp = []
            #                 for i in range(t.n):
            #                     temp.append(t.board[i][i])
            #                 if temp.count(" O ") == board_size - 1 and temp.count(" - ") == 1:
            #                     s_row = temp.index(" - ")
            #                     s_col = temp.index(" - ")
            #                 else:
            #                     ## DIAGONAL winning move available? Note; all moves of form (n, n)
            #                     ## top right -> bottom left diagonal
            #                     temp = []
            #                     i = t.n - 1
            #                     while i >= 0:
            #                         temp.append(t.board[t.n - i - 1][i])
            #                         i -= 1
            #                     if temp.count(" O ") == board_size - 1 and temp.count(" - ") == 1:
            #                         s_row = temp.index(" - ")
            #                         s_col = temp.index(" - ")
            #                     else:
            #                         ########### Random ###########
            #                         ######   Server Move  ########
            #                         random.seed()
            #                         end = board_size - 1
            #                         s_row = random.randint(0, end)
            #                         s_col = random.randint(0, end)
            #                         # Catch if it's already taken
            #                         while t.is_taken(s_row, s_col):
            #                             s_row = random.randint(0, end)
            #                             s_col = random.randint(0, end)
            ########### Random ###########
            ######   Server Move  ########
            random.seed()
            end = board_size - 1
            s_row = random.randint(0, end)
            s_col = random.randint(0, end)
            # Catch if it's already taken
            while t.is_taken(s_row, s_col):
                s_row = random.randint(0, end)
                s_col = random.randint(0, end)
                
            # Execute server move, check status
            print("Server move: ")
            t.make_move(" O ", s_row, s_col)
            if t.game_won():
                print("Server wins!")
                break
            elif t.board_full():
                print("Tie game!")
                break
        # Loop back around until win/loss or tie (full board)

def main():
    s = Server()
    s.play()

if __name__ == '__main__':
    main()
