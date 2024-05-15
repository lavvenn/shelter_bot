from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton

admin_panel_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "активные игры", callback_data="get_active_games")],
    [InlineKeyboardButton(text = "комнаты ожидания", callback_data="get_all_waiting_rooms")],
    [InlineKeyboardButton(text = "создать тесовую игру на 5 человек", callback_data="create_test_game")],
])

back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "⬅️назад в админ панель⬅️", callback_data="back_to_admin_panel")]
])