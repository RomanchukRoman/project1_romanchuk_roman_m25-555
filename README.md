# Лабиринт сокровищ


**Описание проекта**  
Текстовая игра-лабиринт на Python. Игрок перемещается по комнатам, собирает предметы, решает загадки и ищет сокровища. Основная цель — найти `treasure_key` и использовать его на `treasure_chest` в комнате `treasure_room`.

---

## Установка и запуск

### Через Poetry
1. Клонируйте репозиторий:
```bash
git clone git@github.com:RomanchukRoman/project1_romanchuk_roman_m25-555.git
cd project1_romanchuk_roman_m25-555
````

2. Установите зависимости и создайте виртуальное окружение:

```bash
poetry install
poetry run project
```

### Через Makefile

```bash
make install
make project
```

---

## Цель игры и процесс

* Исследовать комнаты лабиринта.
* Собрать полезные предметы.
* Решать загадки в комнатах.
* Найти `treasure_key` и использовать его для открытия сундука с сокровищами.
* Игра завершается, когда игрок успешно открывает `treasure_chest` или вводит команду `quit`/`exit`.

---

## Структура проекта

```
project1_romanchuk_roman_m25-555/
├── labyrinth_game/
│   ├── __init__.py
│   ├── main.py            # Основной исполняемый файл
│   ├── constants.py       # Константы (карта комнат)
│   ├── player_actions.py  # Действия игрока (ходы, использование предметов)
│   └── utils.py           # Вспомогательные функции (описание комнаты, решение загадок)
├── pyproject.toml
├── poetry.lock
├── Makefile
└── README.md
```

---

## Автор

Romanchuk Roman
Email: [r.romanchuk@ya.ru](mailto:r.romanchuk@ya.ru)
