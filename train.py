from board import Board
from agent import agent
from board import Color
from player import HumanPlayer, ComputerPlayer

def train():
    game_board = Board
    player1 = agent(Color.Black)
    player2 = ComputerPlayer(Color.White)

    while True:
        state_old = game_board.board
        

