import random
import termcolor


def create_board(hight=41, width=81, space=" ", vert_boarder=" ", horis_boarder=" "):
    board = []
    first_last_row = [0, hight - 1]

    for num in range(hight):
        if num in first_last_row:
            board.append([horis_boarder] * width)
        else:
            board.append([vert_boarder] + [space] * (width - 2) + [vert_boarder])

    return board


"""
–––––––––––––––––––––––––––––––––––––
Board_1
–––––––––––––––––––––––––––––––––––––
"""


def generate_seas():
    seas = []
    hight_and_width = {}

    for num in range(1, 4):
        hight = random.randint(10, 15)
        width = random.randint(15, 30)
        seas.append(create_board(hight, width, " ", "~", "~"))
        hight_and_width[num] = (hight, width)

    return seas, hight_and_width


def random_seas_indices(board_hight, board_width, first_row_col, hight_and_width):
    sea_1_hight, sea_1_width = hight_and_width[1]
    sea_2_hight, sea_2_width = hight_and_width[2]
    sea_3_hight, sea_3_width = hight_and_width[3]

    random_row_1 = random.randint(first_row_col, board_hight - sea_1_hight)

    if random_row_1 > sea_2_hight:
        random_col_1 = random.randint(first_row_col, board_width - sea_2_width)
    else:
        random_col_1 = random.randint(sea_1_width, board_width - sea_2_width)

    random_row_2 = random.randint(sea_2_hight, board_hight - sea_3_hight)

    if random_row_1 + sea_1_hight < random_row_2:
        random_col_2 = random.randint(first_row_col, board_width - sea_3_width)
    else:
        random_col_2 = random.randint(sea_1_width, board_width - sea_3_width)

    return random_row_1, random_col_1, random_row_2, random_col_2


def placing_seas():
    board_hight = 31
    board_width = 81
    first_row_col = 0

    board = create_board(board_hight, board_width)
    available_coordinates = []

    seas, hight_and_width = generate_seas()
    sea_1, sea_2, sea_3 = seas
    row_1, col_1, row_2, col_2 = random_seas_indices(board_hight, board_width, first_row_col, hight_and_width)

    board, yellow1_green1_whirlpools, available_coordinates = placing_1st_sea(board, sea_1, row_1,
                                                                              available_coordinates, hight_and_width[1])
    board, blue1_yellow_2_whirlpools, available_coordinates = placing_2nd_sea(board, sea_2, col_1,
                                                                              available_coordinates, hight_and_width[2])
    board, green2_blue_2_whirlpools, available_coordinates = placing_3rd_sea(board, sea_3, row_2, col_2,
                                                                             available_coordinates, hight_and_width[3])

    whirlpools_dict = gen_whirlpools_dict(
        yellow1_green1_whirlpools + blue1_yellow_2_whirlpools + green2_blue_2_whirlpools)

    return board, available_coordinates, whirlpools_dict


def gen_whirlpools_dict(whirlpools):
    whirlpools_dict = {}

    for n in range(len(whirlpools) // 2):
        whirlpools_dict[whirlpools[n]] = whirlpools[n + 3]
        whirlpools_dict[whirlpools[n + 3]] = whirlpools[n]

    return whirlpools_dict


def placing_1st_sea(board, sea_1, row_1, available_coordinates, dimensions):
    row_for_sea = row_1

    for row_num in range(len(sea_1)):
        n = 0
        for el in sea_1[row_num]:
            board[row_1][n] = el
            available_coordinates.append((row_1, n))
            n += 1
        row_1 += 1

    board, sea_indices = sea_1_whirlpools(board, dimensions, row_for_sea)

    return board, sea_indices, available_coordinates


def placing_2nd_sea(board, sea_2, col_1, available_coordinates, dimensions):
    col_for_whirlpool = col_1

    for row_num in range(len(sea_2)):
        n = 0
        r_col = col_1
        for col in sea_2[row_num]:
            board[row_num][r_col] = col
            available_coordinates.append((row_num, r_col))
            r_col += 1
            n += 1

    board, whirlpool_indices = sea_2_whirlpools(board, dimensions, col_for_whirlpool)

    return board, whirlpool_indices, available_coordinates


def placing_3rd_sea(board, sea_3, row_2, col_2, available_coordinates, dimensions):
    row_for_whirlpool = row_2
    col_for_whirlpool = col_2

    for row_num in range(len(sea_3)):
        col = col_2
        for el in sea_3[row_num]:
            board[row_2][col] = el
            available_coordinates.append((row_2, col))
            col += 1
        row_2 += 1

    board, whirlpool_indices = sea_3_whirlpools(board, dimensions, row_for_whirlpool, col_for_whirlpool)

    return board, whirlpool_indices, available_coordinates


"""
–––––––––––––––––––––––––––––––––––––
Board_2
–––––––––––––––––––––––––––––––––––––
"""


def sec_board(board):
    road_banch = [14, 18, 22]

    for index in road_banch:
        board[index][1: 80] = ["–"] * 79

    return board, board_all_indices(board)


def mermaids_placement(board):
    mermaid = 20

    while mermaid > 0:
        road_indices = [15, 16, 17, 19, 20, 21]
        row_index = random.choice(road_indices)
        col_index = random.randint(1, 78)
        if board[row_index][col_index] == " " and board[row_index][col_index + 2] == " ":
            board[row_index][col_index: col_index + 2] = ["M"] * 2
            mermaid -= 1

    return board


def board_all_indices(board):
    board_indices = []

    for row_num in range(len(board)):
        for col_num in range(len(board[row_num])):
            board_indices.append((row_num, col_num))

    return board_indices


"""
–––––––––––––––––––––––––––––––––––––
PRINT
–––––––––––––––––––––––––––––––––––––
"""


def display_board(board):
    for row in board:
        for el in row:
            if el == "K":
                print(termcolor.colored(el, "yellow"), end="")
            elif el == "@":
                print(termcolor.colored(el, "cyan"), end="")
            elif el == "T":
                print(termcolor.colored(el, "green"), end="")

            else:
                print(el, end="")
        print()


"""
–––––––––––––––––––––––––––––––––––––
WHIRLPOOLS
–––––––––––––––––––––––––––––––––––––
"""


def mark_whirlpools(board, whirlpools, first_row, last_row, first_col, last_col, ):
    whirlpool_indices = []

    for whirlpool in whirlpools:
        rows_and_cols = {1: first_row, 2: last_row, 3: first_col, 4: last_col}
        key = random.randint(1, 4)

        if key < 3:
            rand_col = random.randint(first_col + 1, last_col - 2)
            board[rows_and_cols[key]][rand_col] = whirlpool
            whirlpool_indices.append((rows_and_cols[key], rand_col))
        else:
            rand_row = random.randint(first_row + 1, last_row - 2)
            board[rand_row][rows_and_cols[key]] = whirlpool
            whirlpool_indices.append((rand_row, rows_and_cols[key]))

    return board, whirlpool_indices


def sea_1_whirlpools(board, dimensions, rand_row):
    whirlpools = [termcolor.colored("O", "yellow"), termcolor.colored("O", "green")]
    hight, width = dimensions
    first_row = rand_row
    last_row = rand_row + hight - 1
    first_col = 0
    last_col = width - 1

    return mark_whirlpools(board, whirlpools, first_row, last_row, first_col, last_col)


def sea_2_whirlpools(board, dimensions, rand_col):
    whirlpools = [termcolor.colored("O", "blue"), termcolor.colored("O", "yellow")]
    hight, width = dimensions
    first_row = 0
    last_row = hight - 1
    first_col = rand_col
    last_col = rand_col + width - 1

    return mark_whirlpools(board, whirlpools, first_row, last_row, first_col, last_col)


def sea_3_whirlpools(board, dimensions, rand_row, rand_col):
    whirlpools = [termcolor.colored("O", "green"), termcolor.colored("O", "blue")]
    hight, width = dimensions
    first_row = rand_row
    last_row = rand_row + hight - 1
    first_col = rand_col
    last_col = rand_col + width - 1

    return mark_whirlpools(board, whirlpools, first_row, last_row, first_col, last_col)


def main():
    board, available_coordinates = placing_seas()
    display_board(board)
    print(len(available_coordinates))


if __name__ == "__main__":
    main()