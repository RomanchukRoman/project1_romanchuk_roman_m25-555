# labyrinth_game/player_actions.py

from labyrinth_game.constants import ROOMS
from labyrinth_game import utils

def show_inventory(game_state):
    '''
    Функция отображения инвентаря.
    Она должна принимать один аргумент — словарь game_state.
    Прочитайте game_state['player_inventory'] и выведите его содержимое или сообщение о том, что инвентарь пуст.
    '''
    inventory = game_state['player_inventory']
    if inventory:
        print(', '.join(inventory))
    else:
        print('\nВаш инвентарь пуст.')

def get_input(prompt='\nВведите команду > '):
    '''
    Ввод пользователя.
    Так как мы часто будем запрашивать данные у пользователя стоит вынести эту логику в отдельную функцию.
    Функция должна принимать параметр prompt, который выводит текст при пользовательском вводе
    '''
    try:
        user_input = input(prompt).strip().lower()
        return user_input
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"
    
def move_player(game_state, direction):
    '''
    Функция перемещения.
    Она должна принимать два аргумента — game_state и направление (строку, например, 'north').
    Проверяет, существует ли выход в этом направлении.
    Если выход есть:
    Обновите текущую комнату.
    Увеличьте шаг на единицу.
    Выведите описание новой комнаты.
    Если выхода нет, выведите на экран сообщение: "Нельзя пойти в этом направлении."
    '''
    room = game_state['current_room']
    room_data = ROOMS[game_state['current_room']]
    exits = room_data['exits']

    if direction in exits.keys():
        game_state['current_room'] = exits[direction]
        game_state['steps_taken'] += 1

        utils.describe_current_room(game_state)
    else: 
        print('Нельзя пойти в этом направлении.')