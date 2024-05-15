# Shelter Bot

![Shelter](img/shelter.jpg)

## Описание

**Shelter Bot** — это Telegram бот, который переносит популярную настольную игру "Бункер" в формат Telegram. Используя фреймворк [aiogram](https://docs.aiogram.dev/en/latest/), бот позволяет пользователям играть в игру "Бункер" прямо в мессенджере.

## Возможности

- Создание и управление игрой "Бункер" в Telegram
- Поддержка различных игровых команд
- Гибкая настройка и конфигурация

## Установка и настройка

### Требования

- Python 3.7+
- Библиотека aiogram

### Установка

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/shelter_bot.git
    cd shelter_bot
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:
    ```bash
    pip install aiogram
    ```

4. Скопируйте файл конфигурации и отредактируйте его:
    ```bash
    cp config_example.py config.py
    ```

5. В файле `config.py` укажите токен вашего Telegram бота и другие необходимые параметры.

### Запуск

Для запуска бота выполните команду:
```bash
python run.py

Структура проекта

plaintext

shelter_bot/
├── handlers/              # Модули обработчиков
│   ├── admin.py
│   ├── ingame.py
│   └── start.py
├── img/                   # Изображения для бота
│   ├── all_cards.jpg
│   ├── catastrophe.jpg
│   ├── player_card.jpg
│   └── shelter.jpg
├── keyboards/             # Клавиатуры для взаимодействия с пользователем
│   ├── admin_kb.py
│   ├── builders.py
│   ├── inline.py
│   └── reply.py
├── shelter_game/          # Логика игры
│   ├── characteristics.json
│   ├── shelter_utils.py
│   ├── shelter.py
│   ├── shelters.json
│   └── test.py
├── .gitignore
├── Бункер_Правила.pdf      # Правила игры "Бункер"
├── config_example.py       # Пример конфигурационного файла
├── config.py               # Конфигурационный файл (создается пользователем)
├── game_states.py          # Состояния игры
├── genirate_shelters.py    # Скрипт генерации убежищ
├── README.md
└── run.py                  # Главный файл для запуска бота