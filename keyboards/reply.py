from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🆕️начать новую игру")],
        [KeyboardButton(text="🎮присоединится к игре")]
    ]
 , resize_keyboard=True)

rm_kb = ReplyKeyboardRemove()