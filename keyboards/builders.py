from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton


def translate_characteristic(characteristic: str) -> str:
    if characteristic == "profession":
        return "профессия"
    elif characteristic == "biological_characteristics":
        return "био характеристики"
    elif characteristic == "health":
        return "здоровье"
    elif characteristic == "hobby":
        return "хобби"
    elif characteristic == "phobia":
        return "фобия"
    elif characteristic == "character":
        return "характер"
    elif characteristic == "additional_information":
        return "дополнительная информация"
    elif characteristic == "knowledge":
        return "знания"
    elif characteristic == "baggage":
        return "багаж"
    elif characteristic == "action_card":
        return "действие"
    elif characteristic == "condition_card":
        return "состояние"
    else:
        return "нет такой характеристики"

def get_standart_kb(buttons: str | list[str]) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    if type(buttons) == str:
        builder.button(text = buttons)
    else:
        [builder.button(text = button) for button in buttons]
    return builder.as_markup(resize_keyboard=True)

def print_kards(cards: list)->InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    [builder.row(InlineKeyboardButton(text=f"<--{card}-->", callback_data=f"open_card_{card}")) for card in cards]
    # [builder.row(text=f"<--{card}-->", callback_data=f"open{card}") for card in cards]
    return builder.as_markup(resize_keyboard=True)

def open_caracteristic_kb(closed_characteristic: list[str]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    [builder.row(InlineKeyboardButton(text=translate_characteristic(characteristic), callback_data=f"open_characteristic_{characteristic}")) for characteristic in closed_characteristic]
    builder.row(InlineKeyboardButton(text="⬅️назад", callback_data="back_to_card_list"))
    return builder.as_markup(resize_keyboard=True)