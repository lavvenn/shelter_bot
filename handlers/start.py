from aiogram import Router, F, Bot
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from game_states import Game

from shelter_game.shelter_utils import get_random_game, get_random_card

from keyboards import builders as b
from keyboards import reply as r
from keyboards import inline as i

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




#<--main commands-->
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(START_TEXT, reply_markup=r.main_kb)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")


@router.message(Command("id"))
async def cmd_id(message: Message):
    await message.answer(f"id: {message.from_user.id}")


#<--start_game handlers-->
@router.message(F.text == "🆕️начать новую игру")
async def start_game(message: Message, state: FSMContext):
    await state.set_state(Game.configuration)
    await message.answer(f"напишите название игры")


@router.message(Game.configuration)
async def game_configuration(message: Message, state: FSMContext,bot:Bot):
    global all_games

    if not message.text in all_games.keys():
        all_games[message.text] = get_random_game(name = message.text)
        all_games[message.text].add_card(get_random_card(0,message.from_user.id))
    else:
        await message.answer(f"игра с таким названием уже существует")

    await state.update_data(game_name = message.text)
        
    await state.set_state(Game.waiting)
    await message.answer("ожидайте присоединения к игре других игроков\n если набралось необходимимое количество игроков можите нажать 🚀старт", reply_markup=b.get_standart_kb("🚀старт"))
    await message.answer(f"пользователи в игре\n1-@{message.from_user.username}", reply_markup=i.update_users_list_kb)


@router.message(F.text == "🎮присоединится к игре")
async def join_game(message: Message, state: FSMContext):
    await message.answer(f"напишите название игры")
    await state.set_state(Game.join)


@router.message(Game.join)
async def joining_to_game(message: Message, state: FSMContext,bot:Bot):
    global all_games
    if message.text in all_games.keys():
        game = all_games[message.text]

        #len(game.get_users_id())-1 - номер добовляемого игрока игрока
        game.add_card(get_random_card(len(game.get_users_id())-1,message.from_user.id))

        await state.update_data(game_name = message.text)
        await state.set_state(Game.waiting)
        await message.answer("вы ожидаете игроков в игре")

        print(game.get_users_id())

        all_users_member_data = [await bot.get_chat_member(user_id=user_id, chat_id=user_id) for user_id in game.get_users_id()]
        all_users_names = [member_data.user.username for member_data in all_users_member_data]
        users = [f"{i+1}-@{all_users_names[i]}\n" for i in range(len(all_users_names))]

        await message.answer("пользователи в игре\n" + "".join(users), reply_markup=i.update_users_list_kb)
    else:
        await message.answer(f"игры с таким названием не существует")


#<--waiting handlers-->
        
@router.message(Game.waiting)
async def waiting(message: Message, state: FSMContext):
    data = await state.get_data()
    game = data["game_name"]
    await message.answer(f"вы ожидаете игроков в игре :{game}")

@router.callback_query(Game.waiting, F.data == "update_users_list")
async def update_users_list(query: CallbackQuery, state: FSMContext, bot:Bot):
    global all_games

    data = await state.get_data()
    game = all_games[data["game_name"]]
    all_users_member_data = [await bot.get_chat_member(user_id=user_id, chat_id=user_id) for user_id in game.get_users_id()]
    all_users_names = [member_data.user.username for member_data in all_users_member_data]
    users = [f"{i+1}-@{all_users_names[i]}\n" for i in range(len(all_users_names))]

    try:
        await query.message.edit_text("пользователи в игре\n" + "".join(users), reply_markup=i.update_users_list_kb)
        await query.answer()
    except:
        await query.answer()
