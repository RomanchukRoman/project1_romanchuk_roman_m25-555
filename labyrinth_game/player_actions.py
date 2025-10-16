# labyrinth_game/player_actions.py

def show_inventory(game_state):
    '''
    Функция отображения инвентаря.
    Она должна принимать один аргумент — словарь game_state.
    Прочитайте game_state['player_inventory'] и выведите его содержимое или сообщение о том, что инвентарь пуст.
    '''
    inventory = game_state['player_inventory']
    if inventory:
        print(', '.join(inventory))

def get_input(prompt="> "):
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