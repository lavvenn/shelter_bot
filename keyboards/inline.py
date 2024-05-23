from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "⬅️назад к списку карт⬅️", callback_data="back_to_card_list")]
])

start_game_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "🚀старт", callback_data="start_game")]
])

join_game_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "🏁старт", callback_data="join_game")]
])

master_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "📊выгнать игрока", callback_data="kick_kb")],
    [InlineKeyboardButton(text = "👾завершить игру", callback_data="end_game")]
])

# update_users_list_kb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text = "🔄обновить список🔄", callback_data="update_users_list")]
# ])