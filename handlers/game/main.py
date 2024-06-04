from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.fsm.context import FSMContext

from game_states import Game
from keyboards.builders import print_kards, get_standart_kb, open_caracteristic_kb
from keyboards.reply import main_kb
from keyboards.inline import back_kb, join_game_kb
from shelter_game.shelter_utils import print_card, print_my_card, print_shelter, print_catastrophe

from handlers.start import all_games, waiting_rooms

from config import ALL_PLAYERS_IMG, PLAYER_CARD_IMG, SHELTER_IMG, CATASTROPHE_IMG


router = Router()

# <--message handlers-->

@router.message(Game.game, F.text == "⛔️выйти из игры")
async def leave_game(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"вы вышли из игры", reply_markup=main_kb)


# <--callback_query handlers-->
    
@router.callback_query(Game.waiting, F.data == "start_game")
async def game(query: CallbackQuery, state: FSMContext, bot: Bot):
    global all_games, waiting_rooms

    data = await state.get_data()
    game_name = data["game_name"]
    game = all_games[game_name]
    del waiting_rooms[game_name]
    game.start()
    await query.message.delete()
    await query.answer("игра началась")
    [
        await bot.send_message(
            chat_id=chat_id,
            text="вы можете нажать на кнопку 🏁старт для начала игры",
            reply_markup=join_game_kb,
        )
        for chat_id in game.get_users_id()
    ]

    
@router.callback_query(Game.waiting, F.data == "join_game")
async def start_game(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]

    # photo = id all_cards.jpg
    if query.from_user.id == game.get_users_id()[0]:
            await query.message.answer(
            text=f"вы можeте выйти из игры нажав кнопку ⛔️выйти из игры, а так же управлять игрой 🕹панель ведущего",
            reply_markup=get_standart_kb(["⛔️выйти из игры", "🕹панель ведущего"]),
        )
    else:
        await query.message.answer(
            text=f"вы можeте выйти из игры нажав кнопку ⛔️выйти из игры",
            reply_markup=get_standart_kb("⛔️выйти из игры"),
        )
    await query.message.answer_photo(
        photo=ALL_PLAYERS_IMG,
        reply_markup=print_kards(game.get_cards()),
    )
    await state.set_state(Game.game)
    await query.answer("игра началась")
    await query.message.delete()


@router.callback_query(Game.game, F.data.startswith("show_card_"))
async def open_card(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    # 22 - количество символов перед номером карточки в callback_data
    card = game.cards[int(query.data[22:]) - 1]

    # photo = id all_cards.jpg
    photo = PLAYER_CARD_IMG
    if card.user_id == query.from_user.id:
        await query.message.edit_media(
            media=InputMediaPhoto(
                media=photo,
                caption=print_my_card(card),
                reply_markup=open_caracteristic_kb(card.get_closed_characteristic()),
                parse_mode="Markdown",
            ),
            reply_markup=open_caracteristic_kb(card.get_closed_characteristic()),
        )
    else:
        await query.message.edit_media(
            media=InputMediaPhoto(
                media=photo,
                caption=print_card(card),
                reply_markup=open_caracteristic_kb(card.get_closed_characteristic()),
                parse_mode="Markdown",
            ),
            reply_markup=back_kb,
        )


@router.callback_query(Game.game, F.data.startswith("open_characteristic"))
async def open_characteristic(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    card = game.get_card_by_user_id(query.from_user.id)
    card_index = game.cards.index(card)

    all_games[data["game_name"]].cards[card_index].open_characteristic(query.data[20:])

    if card.user_id == query.from_user.id:
        photo = PLAYER_CARD_IMG
        await query.message.edit_media(
            InputMediaPhoto(
                media=photo, caption=print_my_card(card), parse_mode="Markdown"
            ),
            reply_markup=open_caracteristic_kb(card.get_closed_characteristic()),
        )


@router.callback_query(Game.game, F.data == "back_to_card_list")
async def back_to_card_list(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    photo = ALL_PLAYERS_IMG
    await query.message.edit_media(
        InputMediaPhoto(
            media=photo,
        ),
        reply_markup=print_kards(game.get_cards()),
    )


@router.callback_query(Game.game, F.data == "show_shelter")
async def show_shelter(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    photo = SHELTER_IMG
    await query.message.edit_media(
        InputMediaPhoto(
            media=photo,
            caption=print_shelter(game.shelter),
            parse_mode="Markdown",
        ),
        reply_markup=back_kb,
    )


@router.callback_query(Game.game, F.data == "show_catastrophe")
async def show_catastrophe(query: CallbackQuery, state: FSMContext):
    global all_games
    data = await state.get_data()
    game = all_games[data["game_name"]]
    photo = CATASTROPHE_IMG
    await query.message.edit_media(
        InputMediaPhoto(
            media=photo,
            caption=print_catastrophe(game.catastrophe),
            parse_mode="Markdown",
        ),
        reply_markup=back_kb,
    )     