from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from game_states import Game
from keyboards.inline import master_kb
from keyboards.builders import kick_kb

# from final.g4f_final import G4FFinal

from handlers.start import all_games, waiting_rooms

router = Router()

# <--master handlers-->

@router.message(Game.game, F.text == "🕹панель ведущего")
async def master_panel(message: Message, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    if message.from_user.id == game.get_users_id()[0]:
        await message.answer(
            "🕹панель ведущего", reply_markup=master_kb
        ) 
        await message.delete()
    else:
        await message.answer("только ведущий могут управлять игрой")


@router.callback_query(Game.game, F.data == "kick_kb")
async def kick_panel(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    await query.message.edit_text(
        "выберите пользователя для кика или возвращения", reply_markup=kick_kb(game.get_cards())
    )


@router.callback_query(Game.game, F.data == "back_to_master_panel")
async def back_to_master_panel(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    if query.from_user.id == game.get_users_id()[0]:
        await query.message.answer(
            "🕹панель ведущего", reply_markup=master_kb
        ) 
        await query.message.delete()
    else:
        await query.message.answer("только ведущий могут управлять игрой")


@router.callback_query(Game.game, F.data.startswith("kick_"))
async def kick_user(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]

    game.kick_user(int(query.data[5:]) - 1)

    await query.message.edit_text(
        "выберите пользователя для кика или возвращения", reply_markup=kick_kb(game.get_cards())
    )
    await query.answer(f"пользователь {query.data[5:]} кикнут")


@router.callback_query(Game.game, F.data.startswith("reborn_"))
async def kick_user(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]

    game.reborn_user(int(query.data[7:]) - 1)

    await query.message.edit_text(
        "выберите пользователя для кика или возвращения", reply_markup=kick_kb(game.get_cards())
    )
    await query.answer(f"пользователь {query.data[7:]} возвращен")


@router.callback_query(Game.game, F.data == "end_game")
async def end_game(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    final = G4FFinal().get_final(game_data=game.get_final())

    await query.message.answer(
        "в разработке"
    )
    await query.message.delete()

@router.callback_query(Game.game, F.data == "close_master_panel")
async def close_master_panel(query: CallbackQuery, state: FSMContext):
    await query.message.delete()