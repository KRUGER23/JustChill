# Создаем пустое поле 3x3
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Определяем функцию для отрисовки игрового поля
def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

# Определяем функцию для проверки победы
def check_win(board, player):
    # Проверяем строки
    for row in board:
        if row.count(player) == 3:
            return True

    # Проверяем столбцы
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Проверяем диагонали
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # Если ни один из условий не выполнен, возвращаем False
    return False

# Определяем функцию для хода игрока
def player_move(board, player):
    # Получаем координаты клетки, куда игрок хочет поставить свой знак
    row = int(input("Введите номер строки (1-3): ")) - 1
    col = int(input("Введите номер столбца (1-3): ")) - 1

    # Проверяем, что клетка свободна
    if board[row][col] != ' ':
        print("Эта клетка уже занята. Попробуйте еще раз.")
        player_move(board, player)
    else:
        # Ставим знак игрока на выбранную клетку
        board[row][col] = player

# Определяем основную функцию игры
def main():
    print("Добро пожаловать в игру крестики-нолики!")
    print_board(board)

    # Цикл поочередных ходов игроков
    for turn in range(9):
        if turn % 2 == 0:
            player = 'X'
        else:
            player = 'O'

        print(f"Ходит игрок {player}")
        player_move(board, player)
        print_board(board)

        # Проверяем, есть ли победитель
        if check_win(board, player):
            print(f"Игрок {player} победил!")
            return

    # Если все клетки заняты и нет победителя, объявляем ничью
    print("Ничья!")

# Запускаем игру
main()
