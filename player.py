import random
import pygame

class Player: # 玩家抽象类
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        raise NotImplementedError("This method should be overridden by subclasses")

class ComputerPlayer(Player): # 计算机玩家【随机移动】
    def __init__(self, color):
            super().__init__(color)
    
    def get_move(self, board):
        # 找到所有合法的空位
        legal_moves = [(x, y) for x in range(3) for y in range(3) if board.legal_move(x, y)]
        
        if not legal_moves:
            raise Exception("There are no legal moves")

        # 从合法的移动中随机选择一个
        x, y = random.choice(legal_moves)
        print(f"{self.color.name} move: {[x, y]}")
        # 执行移动
        board.make_move(x, y, self.color)
        return 

class HumanPlayer(Player):  # 人类玩家
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board):
        move_made = False
        while not move_made:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # 这里需要确保'running'变量在外部可以正确处理
                    pygame.quit()  # 退出pygame
                    return None  # 或抛出异常以终止程序
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1 代表鼠标左键
                        x, y = pygame.mouse.get_pos()
                        print(f"Mouse clicked at ({x}, {y})")
                        x1, y1 = x // board.BLOCK_SIZE, y // board.BLOCK_SIZE
                        if board.legal_move(x1, y1):  # 确认点击位置是否为合法移动
                            print(f"{self.color.name} move: {[x1, y1]}")
                            board.make_move(x1, y1, self.color)
                            move_made = True  # 更新状态，表示已完成移动
                            return (x1, y1)  # 返回有效的移动位置

