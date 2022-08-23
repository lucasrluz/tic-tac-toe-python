import sys


def index():
    while True:
        print("TIC TAC TOE\n[1] - Jogar\n[0] - Sair")

        option = input("Opção: ")

        if option == "1":
            break
        if option == "0":
            sys.exit()
        else:
            continue


def setPlayers(players):
    while True:
        print(
            "Qual jogador vai começar jogando?\n[1] - X\n[2] - O\n[0] - Sair")

        option = input("Opção: ")

        if option == "1":
            players[0] = "X"
            players[1] = "O"
            break

        if option == "2":
            players[0] = "O"
            players[1] = "X"
            break

        if option == "0":
            sys.exit()

        else:
            continue


def play(turn, players, player_turn, board):
    while True:
        if turn is True:
            turn = False
            player_turn = players[0]

        elif turn is False:
            turn = True
            player_turn = players[1]

        print(f" {board[0]} | {board[1]} | {board[2]}\n---+---+---\n {board[3]} | {board[4]} | {board[5]}\n---+---+---\n {board[6]} | {board[7]} | {board[8]}")

        print(f"Em qual posição o jogar {player_turn} vai jogar?")

        move = int(input("Opção: "))

        if board[move] != "X" and board[move] != "O":
            board[move] = player_turn

        if board[0] == board[3] == board[6]:
            print(f"Jogador {player_turn} venceu!")
            main()

        if board[0] == board[4] == board[8]:
            print(f"Jogador {player_turn} venceu!")
            main()

        if board[0] == board[1] == board[2]:
            print(f"Jogador {player_turn} venceu!")
            main()

        if board[1] == board[4] == board[7]:
            print(f"Jogador {player_turn} venceu!")
            main()

        if board[2] == board[4] == board[6]:
            print(f"Jogador {player_turn} venceu!")
            main()

        if board[2] == board[5] == board[8]:
            print(f"Jogador {player_turn} venceu!")
            main()

        if board[3] == board[4] == board[5]:
            print(f"Jogador {player_turn} venceu!")
            main()

        if board[6] == board[7] == board[8]:
            print(f"Jogador {player_turn} venceu!")
            main()


def main():
    players = ["", ""]

    player_turn = players[1]

    turn = True

    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    index()
    setPlayers(players)
    play(turn, players, player_turn, board)


main()
