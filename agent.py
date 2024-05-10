import torch
import random
from player import Player, ComputerPlayer
from collections import deque
from model import Linear_QNet, QTrainer
import numpy as np

MAX_MEMORY = 100_000
LR = 0.001
BATCH_SIZE = 32

class agent(Player):
    def __init__(self): #初始化
        super().__init__(color)
        self.load_model()
        self.n_games = 0
        self.epsilon = 1 # randomness
        self.gamma = 0.4 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)
        self.reward_win = 10
        self.reward_lose = -10
        self.reward_draw = 5

    def evaluate_game(self, board): # 评估游戏
        # 根据游戏结果返回相应的奖励
        if board.check_winner(self.color):
            return self.reward_win

    def load_model(self): #加载模型
        if os.path.exists("./model/model.pth"):
            self.model = torch.load("./model/model.pth", map_location='cpu')
            print("model loaded")
        else:
            print("No model found, initialized new model")
            self.model = Linear_QNet(11, 256, 9)

    def get_state(self, board): # 获取状态
        state = board.get_state()
        return state
    
    def remember(self, state, action, reward, next_state, done): # 记忆
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self): #长记忆
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        state, actions, rewards, next_state, dones = zip(*mini_sample)
        self.trainer.train_step(state, actions, rewards, next_state, dones)

    def train_short_memory(self, state, action, reward, next_state, done): # 短记忆
        self.trainer.train_step(state, action, reward, next_state, done)


    def get_action(self, board): # 获取动作
        move_made = False
        self.epsilon = 1 - self.n_games * 0.0001
        while not move_made: 
            if np.random.random() < self.epsilon: # 随机动作
                ComputerPlayer.get_move(self, board)
                move_made = True
            else: # 选择最优动作
                state0 = torch.tersor(self.get_state(board), dtype=torch.float)
                prediction = self.model(state0)
                move = torch.argmax(prediction).item()
                board.make_move(move, self.color)
                move_made = True

    
            
    

