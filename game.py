from board import Board, Color
from player import HumanPlayer, ComputerPlayer
import time
#from agent import agent

def play_game(player1, player2):
    game_board = Board()  # 创建棋盘
    current_player = player1 if Color.Black == player1.color else player2  # 确定初始玩家
    
    reward = 0

    game_running = True
    while game_running:        
        game_board._update_ui()
        time.sleep(0.5)

        step_result = play_step(current_player, game_board)
        if not step_result["continue"]:
            print(step_result["message"])
            reward = reward + step_result["reward"]
            print(reward)
            break
        else:
            reward = reward + step_result["reward"]
            print(reward)
        # 切换玩家
        current_player = player2 if current_player == player1 else player1

        print(game_board.board)

  
def play_step(current_player, game_board):
    # 当前玩家进行移动
    current_player.get_move(game_board)

    # 检查游戏是否结束：胜利或者平局
    if game_board.check_winner(current_player.color):  # 检查当前玩家是否胜利
        print(f"{current_player.color.name} wins!")
        game_board._update_ui()
        time.sleep(5)
        return {"continue": False, "reward": 10, "message": "Win"}

    if game_board.is_full():  # 检查棋盘是否已满
        print("Game is a draw")
        game_board._update_ui()
        time.sleep(3)
        return {"continue": False, "reward": 5, "message": "Draw"}

    return {"continue": True, "reward": 1, "message": "Continue"}  



def __main__():
    # 设置玩家
    userinput = input("Do you want to play against the computer? (y/n)")
    if userinput == "y":
        gofirst = input("Do you want to go first? (y/n)")
        whetherAI = input("Do you want to play against the advanced computer? (y/n)")

        player1_color = Color.Black if gofirst == "y" else Color.White
        player2_color = Color.White if gofirst == "y" else Color.Black

        if whetherAI == "y":
            player1 = HumanPlayer(player1_color)
            player2 = agent(player2_color)
        else:
            player1 = HumanPlayer(player1_color)
            player2 = ComputerPlayer(player2_color)


    elif userinput == "n":
        player1 = ComputerPlayer(Color.Black)
        player2 = ComputerPlayer(Color.White)

    # 开始游戏
    play_game(player1, player2)


if __name__ == "__main__":
    __main__()