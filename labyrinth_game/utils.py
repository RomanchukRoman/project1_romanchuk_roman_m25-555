# labyrinth_game/utils.py

from labyrinth_game.constants import ROOMS

def describe_current_room(game_state):
    '''
    Функция описания комнаты
    Она должна принимать один аргумент — словарь game_state.
    Используя game_state['current_room'], получите из константы ROOMS данные о текущей комнате.
    Последовательно выведите на экран:
    Название комнаты в верхнем регистре (например, == ENTRANCE ==).
    Описание комнаты.
    Список видимых предметов. Если они есть, то вывести сообщение "Заметные предметы:" с перечисленными предметами
    Доступные выходы("Выходы:").
    Сообщение о наличии загадки, если она есть("Кажется, здесь есть загадка (используйте команду solve).")
    '''
    room = game_state['current_room']
    room_data = ROOMS[game_state['current_room']]
    description = room_data['description']
    items = room_data['items']
    exits = room_data['exits']
    puzzle = room_data['puzzle']

    print(f'\n== {room.upper()} ==')
    print(description)
    if items:
        print(f"Заметные предметы: {', '.join(items)}")
    print(f"Выходы: {', '.join(exits.keys())}")
    if puzzle:
        print('Кажется, здесь есть загадка (используйте команду solve).')
    print('\n')