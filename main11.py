# Создаем пустое поле 3x3
board = [[' ' for _ in range(3)] for _ in range(3)]

# Функция для отображения игрового поля
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Функция для проверки состояния игры
def check_game_over():
    # Проверяем все возможные комбинации для победы
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != ' ':
        return board[2][0]

    # Проверяем, если есть пустые клетки
    for row in board:
        if ' ' in row:
            return None

    # Возвращаем "ничью", если все клетки заполнены, но нет победителя
    return "ничья"

# Основной цикл игры
def play_game():
    current_player = 'X'

    while True:
        print("Ход игрока", current_player)
        display_board()

        row = int(input("Введите номер строки (0-2): "))
        col = int(input("Введите номер столбца (0-2): "))

        # Проверяем, что клетка пуста
        if board[row][col] == ' ':
            board[row][col] = current_player

            # Проверяем состояние игры
            result = check_game_over()
            if result is not None:
                display_board()
                if result == "ничья":
                    print("Игра окончилась в ничью.")
                else:
                    print("Игрок", result, "победил!")
                break

            # Переключаем игрока
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Клетка занята. Попробуйте еще раз.")

# Запускаем игру
play_game()
