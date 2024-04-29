from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "⬅️назад к списку карт⬅️", callback_data="back_to_card_list")]
])

update_users_list_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "🔄обновить список🔄", callback_data="update_users_list")]
])