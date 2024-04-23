from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton

def get_standart_kb(buttons: str | list[str]) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    if type(buttons) == str:
        builder.button(text = buttons)
    else:
        [builder.button(text = button) for button in buttons]
    return builder.as_markup(resize_keyboard=True)

def print_kards(cards: list)->InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    [builder.row(InlineKeyboardButton(text=f"<--{card}-->", callback_data=f"open{card}")) for card in cards]
    # [builder.row(text=f"<--{card}-->", callback_data=f"open{card}") for card in cards]
    return builder.as_markup(resize_keyboard=True)