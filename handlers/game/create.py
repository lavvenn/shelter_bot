from random import randint

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from game_states import Game

from shelter.shelter_utils import get_random_game, get_random_card

from keyboards import builders as b
from keyboards import reply as r
from keyboards import inline as i

from handlers.start import all_games, waiting_rooms


router = Router()

# <--start_game handlers-->
@router.message(F.text == "🆕️начать новую игру")
async def start_game(message: Message, state: FSMContext):
    await state.set_state(Game.configuration)
    await message.answer(f"вы можете отменить создание игры нажав кнопку 📛отмена", reply_markup=b.get_standart_kb("📛отмена"))
    await message.answer(f"нвыберите через что генирировать финал", reply_markup=b.gpt_choice_kb())


@router.message(Game.configuration, F.text == "📛отмена")
async def cancel_game(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"игра отменена", reply_markup=r.main_kb)


@router.message(Game.configuration)
async def game_configuration_exeption(message: Message, state: FSMContext, bot: Bot):
    await message.answer("выберите через что генирировать финал")

@router.callback_query(Game.configuration, F.data.startswith("gpt_"))
async def gpt_choice(query: CallbackQuery, state: FSMContext):
    global all_games, waiting_rooms

    game_number = str(randint(100,999))

    if not game_number in all_games.keys():
        all_games[game_number] = get_random_game(name=game_number)
        all_games[game_number].add_card(get_random_card(0, query.from_user.id, query.from_user.full_name))

        await state.update_data(game_name=game_number)

        await state.set_state(Game.waiting)
        await query.message.answer(
            f"ожидайте присоединения к игре {game_number} других игроков\n если набралось необходимимое количество игроков можете нажать 🚀старт",
            reply_markup=i.start_game_kb,
        )
        msg = await query.message.answer(
            f"пользователи в игре {game_number}\n1-@{query.message.from_user.username}"
        )
        waiting_rooms[game_number] = {query.from_user.id: msg.message_id}


    else:
        await query.message.answer("игра с таким названием уже существует, напишите другое название игры или отмените действие") 