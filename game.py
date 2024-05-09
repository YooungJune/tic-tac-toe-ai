import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np
import time

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class color(Enum):
    Black = 1
    White = 2


# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 150
SPEED = 20

class Board:

    def __init__(self, color=color.Black, if_show=False):
        self.w = 450
        self.h = 450
        self.color = color
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Tic-Tac-Toe')
        self.clock = pygame.time.Clock()
        self.show_run = if_show
        self.current_color = color.Black
        self.reset()

    def reset(self):
        # init game state
        self.board = np.zeros((3, 3))
        self.score = 0

    def play_step(self, action):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.show_run = not self.show_run
        
        # 2. move
        if self.color == self.current_color:
            self._move(action) # update the board
           # self.current_color = color.White if self.current_color == color.Black else color.Black



        

        self._update_ui()
        time.sleep(3)


        # if self.lose():
        #     game_over = True
        #     reward = -10
        #     return reward, game_over, self.score

        def initialize_win_conditions():
            return [
                [(0, 0), (0, 1), (0, 2)],  # 第一行
                [(1, 0), (1, 1), (1, 2)],  # 第二行
                [(2, 0), (2, 1), (2, 2)],  # 第三行
                [(0, 0), (1, 0), (2, 0)],  # 第一列
                [(0, 1), (1, 1), (2, 1)],  # 第二列
                [(0, 2), (1, 2), (2, 2)],  # 第三列
                [(0, 0), (1, 1), (2, 2)],  # 对角线从左上到右下
                [(0, 2), (1, 1), (2, 0)]   # 对角线从右上到左下
            ]
        
        def check_winner(board, color):
            board = np.array(board)  # 确保board是numpy数组
            for condition in initialize_win_conditions():
                # 使用tuple unpacking检查棋盘上的每一行/列/对角线
                if all(board[i, j] == color.value for (i, j) in condition):
                    return True
            return False
        
        if check_winner(self.board, self.current_color) == True:
            game_over = True
            reward = 10
            pygame.quit()
            quit()
            return reward, game_over, self.score
        
        def check_draw(board):
            return np.all(board!= 0)
        
        reward = 0
        game_over = False
        print(check_winner(self.board, self.current_color))
        print(self.board , self.current_color)


        # 5. update ui and clock
        if(self.show_run):
            self._update_ui()
            self.clock.tick(SPEED)
        # 6. return game over and score 
        return reward, game_over, self.score

    def _update_ui(self):
        self.display.fill(BLACK)
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 1:
                    pygame.draw.rect(self.display, RED, pygame.Rect(i*BLOCK_SIZE, j*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                elif self.board[i, j] == 2:
                    pygame.draw.rect(self.display, BLUE1, pygame.Rect(i*BLOCK_SIZE, j*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()



    def _move(self, action):
        #place the action on the board
        self.board[action[0], action[1]] = self.color.value
        self.score += 1

if __name__ == "__main__":
    game = TicTacToeAI(if_show=True)
    while True:
        game.play_step([random.randint(0,2),random.randint(0,2)])
        