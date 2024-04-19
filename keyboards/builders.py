from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def print_kards(cards: list)->InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    [builder.button(text=card, callback_data=f"open{card}") for card in cards]
    return builder.as_markup()