from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from game_states import Game

from keyboards import builders as b
from keyboards import reply as r
from keyboards import inline as i

from shelter.shelter_utils import get_random_card

from handlers.start import all_games, waiting_rooms

router = Router()


@router.message(F.text == "🎮присоединится к игре")
async def join_game(message: Message, state: FSMContext):
    await message.answer("напишите название игры")
    await state.set_state(Game.join)


@router.message(Game.join)
async def joining_to_game(message: Message, state: FSMContext, bot: Bot):
    global all_games, waiting_rooms
    if message.text in all_games.keys():
        game = all_games[message.text]

        if not game.started:
            game.add_card(
                get_random_card(len(game.get_users_id()), message.from_user.id, message.from_user.full_name)
            )

            await state.update_data(game_name=message.text)
            await state.set_state(Game.waiting)
            await message.answer(
                "вы ожидаете игроков в игре игра начнётся когда её создатель её  начнёт",
                reply_markup=r.rm_kb,
            )

            print(game.get_users_id())

            all_users_member_data = [
                await bot.get_chat_member(user_id=user_id, chat_id=user_id)
                for user_id in game.get_users_id()
            ]
            all_users_names = [
                member_data.user.username for member_data in all_users_member_data
            ]
            users = [
                f"{i+1}-@{all_users_names[i]}\n" for i in range(len(all_users_names))
            ]

            await message.answer("пользователи в игре\n" + "".join(users))

            for chat_id, message_id in waiting_rooms[message.text].items():
                print(f"{chat_id}  " * 10)
                await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text="пользователи в игре\n" + "".join(users),
                )
            waiting_rooms[message.text][message.from_user.id] = message.message_id

        else:
            if message.from_user.id in game.get_users_id():
                await state.update_data(game_name=message.text)
                await state.set_state(Game.waiting)
                await message.answer(
                    f"вы вернулись в игру", reply_markup=i.join_game_kb
                )

            else:
                await message.answer(
                    f"игра уже началась, вы не можете присоединиться к ней"
                )
    else:
        await message.answer(f"игры с таким названием не существует")