from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from game_states import Game
from keyboards.builders import print_kards, get_standart_kb
from keyboards.reply import main_kb
from keyboards.inline import back_kb

from shelter_game.shelter_utils import  print_card


router = Router()

#<--message handlers-->

@router.message(Game.game, F.text == "🚀старт")
async def game(message: Message, state: FSMContext):
    data = await state.get_data()
    game = data["game"]
    await message.answer(f"вы начали игру", reply_markup=get_standart_kb("⛔️выйти из игры"))
    await message.answer(f"вот карточки игроков", reply_markup=print_kards(game.get_cards()))


@router.message(Game.game, F.text == "⛔️выйти из игры")
async def leave_game(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"вы вышли из игры", reply_markup=main_kb)


#<--callback_query handlers-->

@router.callback_query(Game.game, F.data.startswith("open"))
async def open_card(query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    game = data["game"]
    #17 - количество символов перед номером карточки в callback_data
    card = game.cards[int(query.data[17:])-1]
    await query.message.edit_text(text = print_card(card), reply_markup=back_kb, parse_mode="Markdown")

@router.callback_query(Game.game, F.data == "back_to_card_list")
async def back_to_card_list(query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    game = data["game"]
    await query.message.edit_text(text = f"вот карточки игроков", reply_markup=print_kards(game.get_cards()))
