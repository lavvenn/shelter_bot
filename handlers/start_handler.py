from aiogram import Router, F
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from game_states import Game

from shelter_game.shelter_utils import get_random_game

from keyboards import builders as b

router = Router()

START_TEXT = """
Привет! Я бот для игры в настольную игру "Бункер". 
Для начала нужно создать игру, используя кнопку 🎮начать игру
Если нужна помощь, используй команду /help.

"Бункер" – дискуссионная игра о выживании после апокалипсиса. На Земле грядёт глобальная катастрофа.
Нам повезло, вы оказались перед входом в спасательный бункер, в котором можно пережить самый опасный период.
Но попасть в бункер смогут не все – а лишь половина из вас! За несколько раундов игроки решают, кого НЕ берут в бункер.
Попавшие в бункер – выживут, чтобы затем возродить цивилизацию.
Игроки получают несколько случайных карт характеристик: пол и возраст, профессия, здоровье, хобби и др.
Постепенно вы раскрываете свои карты, знакомитесь друг с другом и принимаете решения, кто и насколько будет полезен для выживания и восстановления жизни после выхода из бункера. 
"""


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(START_TEXT)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")

@router.message(F.text == "🎮начать игру")
async def start_game(message: Message, state: FSMContext):
    await state.set_state(Game.game_configuration)
    await message.answer(f"напишите номер игры")

@router.message(Game.game_configuration)
async def game_configuration(message: Message, state: FSMContext):
    try :
        game_number = int(message.text)
    except:
        await message.answer("Нужно ввести число")

    await state.update_data(game = get_random_game(message.text, 5))
        
    await state.set_state(Game.game)
    await message.answer("вы можете начать игру", reply_markup=b.get_standart_kb("🚀старт"))