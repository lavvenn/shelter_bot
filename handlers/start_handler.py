from aiogram import Router, F
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from game_states import Game

from shelter_game.shelter_utils import get_random_game

from keyboards import builders as b
from keyboards import reply as r

all_games = {}

router = Router()

START_TEXT = """
Привет! Я бот для игры в настольную игру "Бункер". 
Для начала нужно создать игру, используя кнопку 🎮начать игру
Если нужна помощь, используй команду:
/help.

"Бункер" – дискуссионная игра о выживании после апокалипсиса. На Земле грядёт глобальная катастрофа.
Нам повезло, вы оказались перед входом в спасательный бункер, в котором можно пережить самый опасный период.
Но попасть в бункер смогут не все – а лишь половина из вас! За несколько раундов игроки решают, кого НЕ берут в бункер.
Попавшие в бункер – выживут, чтобы затем возродить цивилизацию.
Игроки получают несколько случайных карт характеристик: пол и возраст, профессия, здоровье, хобби и др.
Постепенно вы раскрываете свои карты, знакомитесь друг с другом и принимаете решения, кто и насколько будет полезен для выживания и восстановления жизни после выхода из бункера. 
"""


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(START_TEXT, reply_markup=r.main_kb)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")


@router.message(Command("id"))
async def cmd_id(message: Message):
    await message.answer(f"id: {message.from_user.id}")


@router.message(F.text == "🆕️начать новую игру")
async def start_game(message: Message, state: FSMContext):
    await state.set_state(Game.game_configuration)
    await message.answer(f"напишите название игры")


@router.message(Game.game_configuration)
async def game_configuration(message: Message, state: FSMContext):
    global all_games

    if not message.text in all_games.keys():
        all_games[message.text] = get_random_game(name = message.text, number_of_cards = 5)
    else:
        await message.answer(f"игра с таким названием уже существует")

    await state.update_data(game = all_games[message.text])
        
    await state.set_state(Game.game)
    await message.answer("вы можете начать игру", reply_markup=b.get_standart_kb("🚀старт"))

@router.message(F.text == "🎮присоединится к игре")
async def join_game(message: Message, state: FSMContext):
    await message.answer(f"напишите название игры")
    await state.set_state(Game.join_game)

@router.message(Game.join_game)
async def joining_to_game(message: Message, state: FSMContext):
    global all_games
    if message.text in all_games.keys():
        await state.update_data(game = all_games[message.text])
        await state.set_state(Game.game)
        await message.answer("вы можете начать игру", reply_markup=b.get_standart_kb("🚀старт"))
    else:
        await message.answer(f"игры с таким названием не существует")
