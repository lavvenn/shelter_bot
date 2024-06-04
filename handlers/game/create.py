from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from game_states import Game

from shelter_game.shelter_utils import get_random_game, get_random_card

from config import GAME_RULES

from keyboards import builders as b
from keyboards import reply as r
from keyboards import inline as i

from handlers.start import all_games, waiting_rooms


router = Router()

# <--start_game handlers-->
@router.message(F.text == "🆕️начать новую игру")
async def start_game(message: Message, state: FSMContext):
    await state.set_state(Game.configuration)
    await message.answer(f"напишите название игры")


@router.message(Game.configuration, F.text == "📛отмена")
async def cancel_game(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"игра отменена", reply_markup=r.main_kb)


@router.message(Game.configuration)
async def game_configuration(message: Message, state: FSMContext, bot: Bot):
    global all_games, waiting_rooms

    if not message.text in all_games.keys():
        all_games[message.text] = get_random_game(name=message.text)
        all_games[message.text].add_card(get_random_card(0, message.from_user.id, message.from_user.full_name))

        await state.update_data(game_name=message.text)

        await state.set_state(Game.waiting)
        await message.answer(
            "ожидайте присоединения к игре других игроков\n если набралось необходимимое количество игроков можете нажать 🚀старт",
            reply_markup=i.start_game_kb,
        )
        msg = await message.answer(
            f"пользователи в игре\n1-@{message.from_user.username}"
        )
        waiting_rooms[message.text] = {message.from_user.id: msg.message_id}


    else:
        await message.answer("игра с таким названием уже существует, напишите другое название игры или отмените действие",
                              reply_markup=b.get_standart_kb("📛отмена"))