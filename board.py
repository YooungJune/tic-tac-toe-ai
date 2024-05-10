import numpy as np
from enum import Enum
import pygame

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

class Color(Enum):
    Black = 1
    White = 2
    Empty = 0

class Board:
    def __init__(self): # 初始化3x3的棋盘，全部为空
        self.board = np.full((3, 3), Color.Empty.value) 
        self.w = 450
        self.h = 450 
        self.BLOCK_SIZE = 150
        self.speed = 20
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Tic-Tac-Toe')
        self.clock = pygame.time.Clock()

    def reset(self):  # 重置棋盘
        self.board = np.full((3, 3), Color.Empty.value) 

    def legal_move(self, x, y): # 判断位置是否合法
        return True if self.board[x, y] == Color.Empty.value else False

    def make_move(self, x, y, color): # 落子
        if self.legal_move(x, y):
            self.board[x, y] = color.value

    def is_full(self): # 判断棋盘是否已满
        return np.all(self.board != Color.Empty.value)

    def initialize_win_conditions(self):
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
    
    def check_winner(self, color):
        board = np.array(self.board)  # 确保board是numpy数组
        for condition in self.initialize_win_conditions():
            # 使用tuple unpacking检查棋盘上的每一行/列/对角线
            if all(board[i, j] == color.value for (i, j) in condition):
                return True, color.value

    def _update_ui(self):
        self.display.fill(BLACK)
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 1:
                    pygame.draw.rect(self.display, RED, pygame.Rect(i*self.BLOCK_SIZE+3, j*self.BLOCK_SIZE+3, self.BLOCK_SIZE-3, self.BLOCK_SIZE-3))
                elif self.board[i, j] == 2:
                    pygame.draw.rect(self.display, BLUE1, pygame.Rect(i*self.BLOCK_SIZE+3, j*self.BLOCK_SIZE+3, self.BLOCK_SIZE-3, self.BLOCK_SIZE-3))
        pygame.display.flip()
        return
