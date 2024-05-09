from board import Board, Color
from player import HumanPlayer, ComputerPlayer
import time

current_color = Color.Black

def play_game(player1, player2):
    game_board = Board()
    current_player = player1

    while True:        
        game_board._update_ui()
        time.sleep(0.5)

        # 当前玩家进行移动
        current_player.get_move(game_board)

        # 检查游戏是否结束：胜利或者平局
        if game_board.check_winner(current_player.color):  # 检查当前玩家是否胜利
            print(f"{current_player.color.name} wins!")
            game_board._update_ui()
            time.sleep(5)
            break  # 跳出循环，游戏结束

        if game_board.is_full():  # 检查棋盘是否已满
            print("Game is a draw")
            game_board._update_ui()
            time.sleep(0.5)
            break  # 跳出循环，游戏结束

        # 切换玩家
        current_player = player2 if current_player == player1 else player1

        print(game_board.board)
  


def __main__():
    # 设置玩家
    userinput = input("Do you want to play against the computer? (y/n)")
    if userinput == "y":
        player1 = HumanPlayer(Color.Black)
        player2 = ComputerPlayer(Color.White)
        print("You are playing against the computer")
    elif userinput == "n":
        player1 = ComputerPlayer(Color.Black)
        player2 = ComputerPlayer(Color.White)

    # 开始游戏
    play_game(player1, player2)


if __name__ == "__main__":
    __main__()