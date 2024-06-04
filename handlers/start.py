from aiogram import Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message

from config import GAME_RULES

from keyboards import reply as r


all_games = {}

waiting_rooms = {}

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


# <--main commands-->
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(START_TEXT, reply_markup=r.main_kb)


@router.message(Command("help"))
async def cmd_help(message: Message):
    
    await message.answer("🔽c правилами игры вы можите ознокомится тут🔽")
    await message.answer_document(GAME_RULES)


@router.message(Command("id"))
async def cmd_id(message: Message):
    await message.answer(f"id: {message.from_user.id}")




# # <--waiting handlers-->


# @router.callback_query(Game.waiting, F.data == "update_users_list")
# async def update_users_list(query: CallbackQuery, state: FSMContext, bot: Bot):
#     global all_games

#     data = await state.get_data()
#     game = all_games[data["game_name"]]
#     all_users_member_data = [
#         await bot.get_chat_member(user_id=user_id, chat_id=user_id)
#         for user_id in game.get_users_id()
#     ]
#     all_users_names = [
#         member_data.user.username for member_data in all_users_member_data
#     ]
#     users = [f"{i+1}-@{all_users_names[i]}\n" for i in range(len(all_users_names))]

#     try:
#         await query.message.edit_text(
#             "пользователи в игре\n" + "".join(users),
#             reply_markup=i.update_users_list_kb,
#         )
#         await query.answer()
#     except:
#         await query.answer()


# TODO: #32940378
# <--exception handlers--> не работают т.к в aiogram 3 хендлеры без сосотояния срабатывают на каждом состоянии

# @router.message()
# async def mseesage_exception(message: Message):
#     await message.answer(f"извините я не могу понять ваш запрос для того чтобы перезапустить бота нажмите нажмите /start")

# @router.callback_query()
# async def callback_exception(query: CallbackQuery):
#     await query.message.answer(f"извините я не могу понять ваш запрос для того чтобы перезапустить бота нажмите нажмите /start")
#     await query.answer("нажмите /start")
