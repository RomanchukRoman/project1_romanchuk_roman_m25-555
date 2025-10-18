#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS
from labyrinth_game import player_actions, utils

game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
  }

# Основная игровая функция
def main():
    print('\nДобро пожаловать в Лабиринт сокровищ!')
    utils.describe_current_room(game_state)

    # Цикл запрашивающий команду пока не введено - quit или exit
    while not game_state['game_over']:
        # Вызов функции пользовательского ввода команды 
        command = player_actions.get_input()
        process_command(game_state, command)


def process_command(game_state, command):
    '''
    Обработка команд.
    Функция process_command должна принимать game_state и введенную пользователем строку.
    Внутри нее разделите строку на части, чтобы отделить команду от аргумента (например, 'go north' -> 'go', 'north').
    Используя match / case, определите, какую команду ввел пользователь (look, use, go, take, inventory, quit).
    Вызовите соответствующую функцию (describe_current_room, move_player, take_item и т.д.) в рамках условия, передав ей нужный аргумент.
    В цикле while в функции main() вызывайте process_command для каждой введенной пользователем строки. Убедитесь, что команда quit или exit завершает игру.
    '''
    parts = command.split()
    # первое слово — команда
    action = parts[0]
    arg = parts[1:]

    match action:
        case 'look':
            utils.describe_current_room(game_state)
        case 'use':
            if arg:
                item_name = arg[0]
                player_actions.use_item(game_state, item_name)
        case 'go':
            if arg:
                direction = arg[0]
                player_actions.move_player(game_state, direction)
        case 'take':
            if arg:
                item_name = arg[0]
                player_actions.take_item(game_state, item_name)
        case 'inventory':
            player_actions.show_inventory(game_state)
        case 'quit':
            print('\nВыход из игры.')
            game_state['game_over'] = True
        case 'exit':
            print('\nВыход из игры.')
            game_state['game_over'] = True

if __name__ == '__main__':
    main()

# poetry run project