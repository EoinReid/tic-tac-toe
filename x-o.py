# xs and os
game_board = {
    "top-L":" ",
    "top-M":" ",
    "top-R":" ",
    "mid-L":" ",
    "mid-M":" ",
    "mid-R":" ",
    "bot-L":" ",
    "bot-M":" ",
    "bot-R":" "
    # xs and os board
    # top-L | top-M | top-R
    # ----------------------
    # mid-L | mid-M | mid-R
    # ----------------------
    # bot-L | bot-M | bot-R
}


def print_board(board):
    print(game_board["top-L"] + " | " + game_board["top-M"] + " | " + game_board["top-R"])
    print("----------")  
    print(game_board["mid-L"] + " | " + game_board["mid-M"] + " | " + game_board["mid-R"])
    print("----------")  
    print(game_board["bot-L"] + " | " + game_board["bot-M"] + " | " + game_board["bot-R"])
    print("\n")



def move(board, player_turn):
    player_one_move = input(turn +" make your move: ")
    board[player_one_move] = player_turn
        
turn = "X"
for v in game_board.values():
    print_board(game_board)
    move(game_board, turn)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"