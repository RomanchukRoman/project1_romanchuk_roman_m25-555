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
        print('\nНельзя пойти в этом направлении.')

def take_item(game_state, item_name):
    '''
    Функция взятия предмета.
    Она должна принимать два аргумента — game_state и название предмета.
    Проверяет, есть ли предмет в комнате.
    Если предмет есть:
    Добавьте его в инвентарь игрока.
    Удалите его из списка предметов комнаты.
    Напечатайте сообщение о том, что игрок подобрал предмет("Вы подняли:").
    Если такого предмета в комнате нет, выведите сообщение: "Такого предмета здесь нет."
    '''
    room = game_state['current_room']
    room_data = ROOMS[game_state['current_room']]
    items = room_data['items']

    if item_name in items:
        game_state['player_inventory'].append(item_name)
        items.remove(item_name)
        print(f'\nВы подняли: {item_name}')
    else:
        print('\nТакого предмета здесь нет.')

def use_item(game_state, item_name):
    '''
    Юзаем предметы. Функция должна проверять, есть ли предмет у игрока, и выполнять уникальное действие для каждого предмета:
    Добавьте проверку на наличие предмета в инвенторе. Если как такого нет, то выведете сообщение(У вас нет такого предмета.)
    torch: выводит сообщение о том, что стало светлее.
    sword: выводит сообщение об уверенности.
    bronze box: выводит сообщение об открытии шкатулки и добавляет 'rusty_key' в инвентарь, если его еще нет в инвенторе, иначе пусто.
    Для остальных предметов выводите сообщение, что игрок не знает, как их использовать.
    '''
    items = game_state['player_inventory']

    if item_name in items:
        match item_name:
            case 'torch':
                print('\nСтало светлее.')
            case 'sword':
                print('\nСтало увереннее.')
            case 'bronze box':
                print('\nШкатулка открыта.')
                if not 'rusty_key' in items:
                    items.append('rusty_key')
            case _:
                print('\nИгрок не знает, как это использовать')
    else:
        print('\nУ вас нет такого предмета.')