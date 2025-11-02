CONNECT_FOUR = 4


class InvalidColumn(Exception):
    pass


class FullColumn(Exception):
    pass


def game_field_print():
    [print(*row) for row in game_field]


def valid_column(col):
    if col > 6 or col < 0:
        raise InvalidColumn


def full_column(matrix, col):
    if matrix[0][col] != 0:
        raise FullColumn


def fill_game_field(matrix, col, current_sign):
    for r in range(len(matrix) - 1, -1, -1):
        if matrix[r][col] == 0:
            matrix[r][col] = current_sign
            return r
    return None


def horizontal_win(matrix, col, row, current_sign):
    points = 1
    for c in range(col + 1, cols):
        if matrix[row][c] == current_sign:
            points += 1
        else:
            break
    for c in range(col - 1, -1, -1):
        if matrix[row][c] == current_sign:
            points += 1
        else:
            break
    return points >= CONNECT_FOUR


def vertical_win(matrix, col, row, current_sign):
    points = 1
    for r in range(row + 1, rows):
        if matrix[r][col] == current_sign:
            points += 1
        else:
            break
    for r in range(row - 1, -1, -1):
        if matrix[r][col] == current_sign:
            points += 1
        else:
            break
    return points >= CONNECT_FOUR


def left_diagonal_win(matrix, col, row, current_sign):
    points = 1
    for i in range(1, CONNECT_FOUR):
        try:
            if matrix[row + i][col - i] == current_sign:
                points += 1
        except IndexError:
            break
    for i in range(1, CONNECT_FOUR):
        try:
            if matrix[row - i][col + i] == current_sign:
                points += 1
        except IndexError:
            break
    return points >= CONNECT_FOUR

def right_diagonal_win(matrix, col, row, current_sign):
    points = 1
    for i in range(1, CONNECT_FOUR):
        try:
            if matrix[row - i][col - i] == current_sign:
                points += 1
        except IndexError:
            break
    for i in range(1, CONNECT_FOUR):
        try:
            if matrix[row + i][col + i] == current_sign:
                points += 1
        except IndexError:
            break
    return points >= CONNECT_FOUR

def is_winner(ma, c, r, s):
    return any([horizontal_win(ma,c,r,s,),
                vertical_win(ma,c,r,s),
                left_diagonal_win(ma,c,r,s),
                right_diagonal_win(ma,c,r,s)])
rows = 6
cols = 7
game_field = [[0 for c in range(cols)] for r in range(rows)]

print("Welcome to 'Connect Four' this is your battle field:")
game_field_print()

player_one = input("First_player - Enter your username: ")
print(f"Hello {player_one} Your sign in the game is 'X'")
player_two = input("Second_player - Enter your username: ")
print(f"Hello {player_two} Your sign in the game is 'V'")
print(f"\nLet's start the game")
current_player = player_one
counter = 0
sign = "X"

while True:
    game_field_print()
    choice = input(f"\n{current_player} choice the column 1-7: ")
    try:
        choice = int(choice) - 1
        valid_column(choice)
        full_column(game_field, choice)
        curr_row = fill_game_field(game_field, choice, sign)
        if is_winner(game_field, choice, curr_row, sign):
            print(f"{current_player} is winner!\n")
            game_field_print()
            break
    except ValueError:
        print("The number of column should be integer between 1 and 7. Please try again !")
        continue
    except InvalidColumn:
        print("The number of column should be between 1 and 7. Please try again !")
        continue
    except FullColumn:
        print("The selected column is full. Please choose another one !")
        continue

    counter += 1
    current_player = player_two if current_player == player_one else player_one
    sign = "V" if sign == "X" else "X"

    if counter == rows * cols:
        print(f"There is no winner today. The {player_one} & {player_two} finished draw.")
        break
