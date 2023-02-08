import random
import display_information
from termcolor import colored

"""
************************************
            CREATURES
************************************
"""


def create_creatures():
    whale = {'name': "Whale", 'kind': "Enemy", 'health': 2, "min_damage": 1, "max_damage": 1, "num_to_place": 5,
             'pic': "W"}
    mermaid = {'name': "Mermaid", 'kind': "Enemy", 'health': 20, "min_damage": 5, "max_damage": 10, "num_to_place": 15,
               'pic': "M"}
    rocks = {'name': "Rocks", 'kind': "Enemy", 'health': 20, "min_damage": 20, "max_damage": 50, "num_to_place": 5,
             'pic': "^"}
    kraken = {'name': "Kraken", 'kind': "Enemy", 'health': 20, "min_damage": 1, "max_damage": 5, "num_to_place": 5,
              'pic': "%"}
    tia_dalma = {'name': "Tia Dalma", 'kind': "Friend", 'health': 5, "num_to_place": 1, 'pic': "T"}

    return whale, mermaid, rocks, kraken, tia_dalma


def creatures_on_the_board_dicts(creature):
    list_of_creatures = []

    for num in range(creature["num_to_place"]):
        monster = {}
        for key, value in creature.items():
            monster[key] = value
        list_of_creatures.append(monster)

    return list_of_creatures


def random_creatures_locations(board, board_indexes, list_of_creatures):
    floor = " "

    for creature in list_of_creatures:
        value = False
        while value is False:
            row_index, col_index = random.choice(board_indexes)
            if board[row_index][col_index] == floor:
                board[row_index][col_index] = creature["pic"]
                creature["location"] = (row_index, col_index)
                value = True

    return board, list_of_creatures


def non_road_coordinates(board_indices, road_rows):
    row = 0

    for indices in board_indices:
        if indices[row] in road_rows:
            board_indices.remove(indices)

    return board_indices


def mermaid_placement(board, board_indices, list_of_vehiculs):
    vehiculs_to_place = len(list_of_vehiculs)
    road_rows = [15, 16, 17, 19, 20, 21]
    empty = " "
    non_road_indices = non_road_coordinates(board_indices, road_rows)
    min_col = 1
    max_col = 78

    while vehiculs_to_place > 0:
        row_index = random.choice(road_rows)
        col_index = random.randint(min_col, max_col)
        vehicul = list_of_vehiculs[vehiculs_to_place - 1]

        if board[row_index][col_index] == empty and board[row_index][col_index + 2] == empty:
            vehicul = list_of_vehiculs[vehiculs_to_place - 1]
            if vehicul["name"] == "Rocks":
                board[row_index][col_index: col_index + 2] = [vehicul["pic"]] * 2
                vehicul["location"] = (row_index, col_index)
                vehicul["location_2"] = (row_index, col_index + 1)
            elif vehicul["name"] == "Mermaid":
                board[row_index][col_index] = vehicul["pic"]
                vehicul["location"] = (row_index, col_index)
            else:
                random_creatures_locations(board, non_road_indices, [vehicul])
            vehiculs_to_place -= 1

    return board, list_of_vehiculs


def enemy_pics():
    creatures_list = create_creatures()
    enemy_pics = []

    for el in creatures_list:
        if el["kind"] == "Enemy":
            enemy_pics.append(el["pic"])

    return enemy_pics


"""
************************************
            BOSS
************************************
"""


def create_boss():
    global boss
    boss = {'name': "Barbossa", 'species': "Enemy", 'health': 20, "max_health": 20, "min_damage": 2, "max_damage": 7,
            "picture": "B", "size": 5}

    return boss


def put_boss_on_board(boss, board):
    list_of_creatures = [boss]
    boss_size = boss.get("size")
    how_many_rows = len(board)
    first_row = how_many_rows - 6
    first_col = 1

    for row in range(boss_size):
        for col in range(boss_size):
            board[first_row + row][first_col + col] = boss.get("picture")

    return board, list_of_creatures


def print_boss_info():
    global boss

    print(colored(f"Boss's name : {boss['name']}        Health level : {boss['health']}", "blue"))


"""
************************************
            PLAYER
************************************
"""


def create_player():
    global hero
    'Tworzy bohatera wg wyboru użytkownika'
    display_information.choose_hero()
    invalid = True

    while invalid:
        user_choice = input()
        if user_choice == "1":
            hero = {'name': "Jack Sparrow", 'species': "Captain", 'health': 10, 'max_load': 15, "max_health": 25,
                    "min_damage": 2, "max_damage": 5, "picture": "@"}
            invalid = False
        elif user_choice == "2":
            hero = {'name': "Elizabeth Swann", 'species': "Magic Captain", 'health': 15, 'max_load': 10,
                    'skill': "magic",
                    "max_health": 25, "min_damage": 0, "max_damage": 7, "picture": "@"}
            invalid = False
        elif user_choice == "3":
            hero = {'name': "Will Turner", 'species': "Invisible Captain", 'health': 5, 'max_load': 5,
                    'skill': "invisible", "max_health": 25, "min_damage": 10, "max_damage": 25, "picture": "@"}
            invalid = False
        else:
            print(colored("Choose 1, 2 or 3", "cyan"))
    return hero


def put_player_on_board(board):
    global hero
    player_icon = hero.get("picture")
    wall = "~"
    hero_num = 0

    for row in range(len(board) - 1):
        for col in range(len(board[row]) - 1):
            if board[row][col] == wall and board[row + 1][col] == wall and wall == board[row][
                col + 1] and hero_num != 1:
                player_start_row = row + 1
                player_start_col = col + 2
                board[player_start_row][player_start_col] = player_icon
                hero_num += 1

    return board


def is_it_alive():
    if hero["health"] <= 0:
        display_information.print_end_game()
        return False
    return True


def print_player_info():
    print(colored(f"Captain's name : {hero['name']}     Health level : {hero['health']}", "blue"))


"""
************************************
            FIGHT
************************************
"""


def mermaid_crash(board, obstacle, current_possition, obstacles_dict):
    global hero
    above_road_boarder = 13
    current_row, current_col = current_possition

    if obstacle == "vehiculs":
        board[current_row][current_col] = obstacles_dict["empty_space"]
        board[above_road_boarder][current_col] = hero["picture"]
        hero["location"] = (above_road_boarder, current_col)

    return board


def who_is_the_oponent(list_of_creatures, location):
    for creature in list_of_creatures:
        if location == creature["location"] or (creature["name"] == "Rocks" and location == creature["location_2"]):
            return list_of_creatures.index(creature)
        elif location == hero.get("location"):
            return False


def carry_damage(attacker, opponent):
    damage = random.randint(attacker["min_damage"], attacker["max_damage"])
    opponent["health"] -= damage

    if opponent["health"] > 0:
        return opponent
    else:
        return False


def did_it_hit():
    hit = [True, False]
    return random.choice(hit)


def hit_the_opponent(attacker, opponent):
    if did_it_hit():
        opponent = carry_damage(attacker, opponent)
        return opponent if opponent else None
    else:
        print(colored("You missed, sucker!", "blue"))
        return False


def fight(board, attacker, list_of_creatures, location):
    global hero
    row, col = location
    creature_index = who_is_the_oponent(list_of_creatures, location)

    if creature_index:
        opponent = list_of_creatures[creature_index]
        opponent = hit_the_opponent(attacker, opponent)
        if opponent:
            list_of_creatures[creature_index] = opponent
        elif opponent is None and opponent != hero:
            list_of_creatures.remove(list_of_creatures[creature_index])
            board[row][col] = " "
    else:
        opponent = hero
        opponent = hit_the_opponent(attacker, opponent)
        if opponent:
            hero = opponent

    return board, list_of_creatures


def fight_boss(weapon=None):
    global hero
    global boss

    if weapon is None:
        hero["health"] = 0
        print(colored("Barbossa wins!", "blue"))

    elif weapon == "Tia Dalma":
        boss["health"] = 0

    elif weapon.get("name") == "Canon Ball":
        if did_it_hit():
            boss = carry_damage(hero, boss)
        else:
            hit_hero = did_it_hit()
            if stone_throw() and hit_hero:
                hero["health"] -= boss["max_damage"]
            elif hit_hero:
                hero = carry_damage(boss, hero)

    if win_the_game(boss["health"]):
        exit()

    return boss


def stone_throw():
    number = random.randint(1, 5)
    return number % 3 == 0


def win_the_game(boss_health):
    if boss_health == 0 and hero.get("health") > 0:
        display_information.win_screen()
        return True
    else:
        return False

print(put_boss_on_board())