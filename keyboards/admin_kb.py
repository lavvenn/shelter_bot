from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton

admin_panel_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "активные игры", callback_data="get_active_games")],
    [InlineKeyboardButton(text = "комнаты ожидания", callback_data="get_all_waiting_rooms")]
])

back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "⬅️назад в админ панель⬅️", callback_data="back_to_admin_panel")]
])