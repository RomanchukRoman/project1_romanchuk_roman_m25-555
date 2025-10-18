# labyrinth_game/utils.py

from labyrinth_game.constants import ROOMS
from labyrinth_game import player_actions

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

def solve_puzzle(game_state):
    """
    Функция решения загадок. 
    Сначала проверьте, есть ли загадка в текущей комнате. Если нет, выведите сообщение "Загадок здесь нет." и завершите выполнение функции.
    Если загадка есть, выведите на экран вопрос.
    Получите ответ от пользователя("Ваш ответ: ").
    Сравните ответ пользователя с правильным ответом.
    Если ответ верный:
    Сообщите игроку об успехе.
    Уберите загадку из комнаты, чтобы ее нельзя было решить дважды.
    Добавьте игроку награду.
    Если ответ неверный, сообщите об этом игроку("Неверно. Попробуйте снова.").
    """
    room = game_state['current_room']
    room_data = ROOMS[room]
    puzzle = room_data['puzzle']

    if not puzzle:
        print("Загадок здесь нет.")
        return

    question, correct_answer = puzzle
    print(f"Загадка: {question}")

    # Получаем ответ от игрока
    answer = player_actions.get_input()

    # Сравниваем ответ
    if answer == correct_answer:
        print("Правильно! Вы успешно решили загадку.")
        # Убираем загадку из комнаты
        room_data['puzzle'] = None

        # Добавляем награду 
        reward = 'candy'
        if reward not in game_state['player_inventory']:
            game_state['player_inventory'].append(reward)
            print(f"Вы получили {reward}!")
    else:
        print("Неверно. Попробуйте снова.")