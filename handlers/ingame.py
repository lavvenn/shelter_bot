from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from game_states import Game
from keyboards.builders import print_kards

import genirate_shelters


router = Router()

@router.message(Game.game)
async def game(message: Message, state: FSMContext):
    await message.answer("игра", reply_markup=print_kards(genirate_shelters.games[0].get_card_names()))