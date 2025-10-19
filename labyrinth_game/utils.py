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
    room_data = ROOMS[room]
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
        print("\nЗагадок здесь нет.")
        return

    question, correct_answer = puzzle
    print(f"\nЗагадка: {question}")

    # Внутренний цикл, нужен при неверных ответах, чтобы не выходило в основной игровой цикл
    while True:
        # Получаем ответ от игрока
        answer = player_actions.get_input()

        if answer in ("quit", "exit"):
            print("\nВы решили прекратить попытки.")
            return

        # Сравниваем ответ
        if answer == correct_answer and room != 'treasure_room':
            print("\nПравильно! Вы успешно решили загадку.")
            # Убираем загадку из комнаты
            room_data['puzzle'] = None

            # Добавляем награду для всех комнат, кроме 'treasure_room'
            reward = 'candy'
            if room != 'treasure_room':
                game_state['player_inventory'].append(reward)
                print(f"\nВы получили {reward}!")
                # выход из цикла после успеха
                break  
        elif answer == correct_answer and room == 'treasure_room':
            print('\nВ сундуке сокровище! Вы победили!')
            game_state['game_over'] = True
            break

        else:
            print("\nНеверно. Попробуйте снова.")


def attempt_open_treasure(game_state):
    '''
    Условие победы. Доработайте логику, чтобы игра завершалась победой.
    Определите условие победы. Основное условие: игрок должен использовать treasure_key на treasure_chest в комнате treasure_room.
    Также возможен случай когда пользователь может попытаться взломать treasure_chest, решив загадку.
    Создайте в utils.py функцию attempt_open_treasure(game_state), которая будет реализовывать логику победы.
    Сценарии, которые нужно учесть в функции:
    Проверка ключа: Проверьте, есть ли у игрока в инвентаре 'treasure_key'.
   
    Если ключ есть, выведите сообщение об успешном открытии замка "Вы применяете ключ, и замок щёлкает. Сундук открыт!", удалите 'treasure_chest' из предметов комнаты, сообщите игроку о победе "В сундуке сокровище! Вы победили!" и установите глобальную переменную game_over в True.
    Предложение ввести код: Если ключа в инвентаре нет, сундук все еще можно открыть кодом.
   
    Спросите у игрока, хочет ли он попробовать ввести код (например, "Сундук заперт. ... Ввести код? (да/нет)").
    Если игрок отвечает "да", запросите у него код.
    Сравните введенный код с правильным ответом из puzzle для текущей комнаты.
    Если код верный, выведите сообщение об успехе, удалите сундук, объявите о победе и установите game_over в True.
    Если код неверный, сообщите об ошибке.
    Если игрок изначально отказался вводить код, выведите сообщение "Вы отступаете от сундука.".
    Если игрок пытается поднять или взять в инвентарь(команда take) 'treasure_chest', то выведите сообщение "Вы не можете поднять сундук, он слишком тяжелый."
    '''
    room = game_state['current_room']
    room_data = ROOMS[room]
    items = room_data['items']
    inventory = game_state['player_inventory']

    if 'treasure_key' in inventory:
        print('\nВы применяете ключ, и замок щёлкает. Сундук открыт!')
        items.remove('treasure_chest')
        print('\nВ сундуке сокровище! Вы победили!')
        game_state['game_over'] = True
    else:
        print('Сундук заперт. ... Ввести код? (да/нет)')
        # Получаем ответ от игрока
        answer = player_actions.get_input()
        if answer == 'да':
            solve_puzzle(game_state)
        elif answer == 'нет':
            print('Вы отступаете от сундука.')

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west/up/down)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение") 