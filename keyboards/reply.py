from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🆕️начать новую игру")],
        [KeyboardButton(text="🎮присоединится к игре")]
    ]
 , resize_keyboard=True)