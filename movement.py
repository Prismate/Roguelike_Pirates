import random
import termcolor
import tia_dalma_talk
import creatures
import inventory
import display_information


def character_position(character_icon, board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == character_icon:
                character_coordinate = [row, col]
                return character_coordinate


def direction_of_movement(key, character_coordinate):
    row = character_coordinate[0]
    col = character_coordinate[1]

    if key.upper() == "W":
        return row - 1, col
    elif key.upper() == "S":
        return row + 1, col
    elif key.upper() == "A":
        return row, col - 1
    elif key.upper() == "D":
        return row, col + 1
    else:
        return row, col


def identify_obstacle(obstacle, obstacles_dict):
    for key, value in obstacles_dict.items():
        if obstacle == value or obstacle in value:
            return key

    return False


def move_to_empty_space(board, current_row, current_col, next_row, next_col, obstacles_dict, player_icon):
    board[current_row][current_col] = obstacles_dict["empty_space"]
    board[next_row][next_col] = player_icon
    creatures.hero["location"] = (next_row, next_col)

    return board


def bumps_on_vehicul(board, obstacle, obstacles_dict, list_of_creatures, current_position, next_position):
    current_row, current_col = current_position
    vehicul_index = creatures.who_is_the_oponent(list_of_creatures, next_position)
    board, list_of_creatures = creatures.fight(board, list_of_creatures[vehicul_index], list_of_creatures,
                                               (current_row, current_col))
    board = creatures.mermaid_crash(board, obstacle, current_position, obstacles_dict)

    return board


def obstacle_move(board, key, obstacle, obstacles_dict, current_position, next_position, list_of_creatures,
                  player_icon):
    current_row, current_col = current_position
    next_row, next_col = next_position
    new_row, new_col = direction_of_movement(key, (next_row, next_col))
    new_obstacle = identify_obstacle(board[new_row][new_col], obstacles_dict)

    if obstacle == "enemies":
        board, list_of_creatures = creatures.fight(board, creatures.hero, list_of_creatures, (next_row, next_col))
    elif new_obstacle == "vehiculs":
        board = bumps_on_vehicul(board, new_obstacle, obstacles_dict, list_of_creatures, current_position,
                                 (new_row, new_col))
    elif obstacle == "empty_space" or obstacle == "player_icon":
        move_to_empty_space(board, current_row, current_col, next_row, next_col, obstacles_dict, player_icon)
    elif obstacle == "road":
        if new_obstacle == "empty_space":
            move_to_empty_space(board, current_row, current_col, new_row, new_col, obstacles_dict, player_icon)
        else:
            board = bumps_on_vehicul(board, new_obstacle, obstacles_dict, list_of_creatures, current_position,
                                     (new_row, new_col))
    elif obstacle == "friends":
        choice = tia_dalma_talk.talking_to_tia_dalma(board)
        if choice == "Continue":
            inventory.add_to_inventory(["Tia Dalma"])
            board[next_row][next_col] = " "
            move_to_empty_space(board, current_row, current_col, next_row, next_col, obstacles_dict, player_icon)

    elif obstacle == "vehiculs":
        bumps_on_vehicul(board, obstacle, obstacles_dict, list_of_creatures, current_position, next_position)
    elif obstacle == "boss":
        creatures.fight_boss()

    return board, list_of_creatures


def moveing_through_whirlpools(board, current_position, obstacles_dict, next_position, possible_coordinates,
                               whirlpools_dict,
                               player_icon):
    current_row, current_col = current_position
    board[current_row][current_col] = obstacles_dict["empty_space"]
    whirlpools_indices = whirlpools_dict[next_position]
    next_row, next_col = getting_off_the_whirlpool(board, whirlpools_indices, possible_coordinates)
    board[next_row][next_col] = player_icon
    creatures.hero["location"] = (next_row, next_col)

    return board


def player_move(board, key, list_of_creatures, inventory_hero, list_of_items, whirlpools_dict, possible_coordinates):
    obstacles_dict = {"empty_space": " ", "wall": "~", "friends": "T", "enemies": ["W", "%"], "vehiculs": ["M", "^"],
                      "road": "–", "whirlpools": whirlpools_dict, "player_icon": "@", "boss": "B"}
    player_icon = obstacles_dict["player_icon"]
    current_position = character_position(player_icon, board)
    next_position = direction_of_movement(key, current_position)
    next_row, next_col = next_position
    obstacle = identify_obstacle(board[next_row][next_col], obstacles_dict)

    if obstacle == "wall":
        board[current_position[0]][current_position[1]] = player_icon
    elif obstacle:
        board, list_of_creatures = obstacle_move(board, key, obstacle, obstacles_dict, current_position, next_position,
                                                 list_of_creatures, player_icon)
    elif next_position in whirlpools_dict:
        board = moveing_through_whirlpools(board, current_position, obstacles_dict, next_position, possible_coordinates,
                                           whirlpools_dict, player_icon)
    else:
        for item in list_of_items:
            if item.get("picture") == board[next_row][next_col]:
                board = inventory.player_interaction(board, item, next_position, current_position)
                break

    return board, list_of_creatures


def getting_off_the_whirlpool(board, whirlpool_indices, possible_coordinates):
    whirlpools = [termcolor.colored("O", "green"), termcolor.colored("O", "blue"), termcolor.colored("O", "yellow")]
    row, col = whirlpool_indices

    if (row + 1, col) in possible_coordinates and board[row + 1][col] != "~" and board[row + 1][col] not in whirlpools:
        return row + 1, col
    elif (row - 1, col) in possible_coordinates and board[row - 1][col] != "~" and board[row - 1][
        col] not in whirlpools:
        return row - 1, col
    elif (row, col + 1) in possible_coordinates and board[row][col + 1] != "~" and board[row][
        col + 1] not in whirlpools:
        return row, col + 1
    elif (row, col - 1) in possible_coordinates and board[row][col - 1] != "~" and board[row][
        col - 1] not in whirlpools:
        return row, col - 1


def random_creature_move(board, list_of_creatures, floor=" "):
    keyboard_keys = ["W", "S", "A", "D"]
    enemy_icons = ["W", "%"]
    player_icon = creatures.hero.get("picture")
    for creature in list_of_creatures:
        random_key = random.choice(keyboard_keys)
        row, col = creature["location"]

        new_row, new_col = direction_of_movement(random_key, creature["location"])

        if board[new_row][new_col] == floor:
            board[new_row][new_col] = board[row][col]
            board[row][col] = floor
            creature["location"] = (new_row, new_col)

        elif board[new_row][new_col] == player_icon or board[new_row][new_col] in enemy_icons:
            board, list_of_creatures = creatures.fight(board, creature, list_of_creatures, (new_row, new_col))

    return board, list_of_creatures


def mermaid_movement(board, list_of_vehiculs):
    floor = " "
    min_col = 1
    max_col = 79

    for vehicul in list_of_vehiculs:
        row, col = vehicul["location"]
        kind = vehicul["name"]

        if kind == "Mermaid":
            board[row][col] = floor
            if col == min_col:
                new_col = max_col
            else:
                new_col = col - 1
            board[row][new_col] = vehicul["pic"]
        elif kind == "Rocks":
            board[row][col: col + 2] = [floor] * 2
            if col == min_col:
                new_col = max_col - 1
            else:
                new_col = col - 1
            board[row][new_col: new_col + 2] = [vehicul["pic"]] * 2
            vehicul["location_2"] = (row, new_col + 1)

        vehicul["location"] = (row, new_col)

    return board, list_of_vehiculs


def creature_movement(board, list_of_creatures):
    first_creature = list_of_creatures[0]

    if first_creature["name"] == "Mermaid" or first_creature["name"] == "Rocks":
        board, list_of_creatures = mermaid_movement(board, list_of_creatures)
    elif first_creature["name"] == "Whale" or first_creature["name"] == "Kraken":
        board, list_of_creatures = random_creature_move(board, list_of_creatures)
    elif first_creature["name"] == "Barbossa":
        board, list_of_creatures = boss_movement(board, list_of_creatures)

    return board, list_of_creatures


def boss_movement(board, list_of_creatures):
    global boss
    boss = creatures.boss
    boss_coordinate = character_position(boss.get("picture"), board)
    first_row = boss_coordinate[0]
    first_col = boss_coordinate[1]
    last_col = first_col + (boss.get("size") - 1)
    lenght_row_board = len(board[first_row])
    movement = 2

    if last_col + movement < lenght_row_board - 2:
        for row in range(boss.get("size")):
            for col in range(movement):
                board[first_row + row][first_col + col] = " "
                board[first_row + row][last_col + (col + 1)] = boss.get("picture")

    else:
        for row in range(boss.get("size")):
            for col in range(boss.get("size")):
                board[first_row + row][first_col + col] = " "

        creatures.put_boss_on_board(boss, board)

    return board, list_of_creatures
