#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS
from labyrinth_game import player_actions, utils

game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
  }

def main():
    print('\nДобро пожаловать в Лабиринт сокровищ!')
    utils.describe_current_room(game_state)

# нужен while
# этот код под вопросом
    command = player_actions.get_input()
    print(f'Вы ввели команду: {command}')
  

if __name__ == '__main__':
    main()
  