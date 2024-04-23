from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from config import ADMINS_LIST

from handlers.start_handler import all_games


router = Router()

@router.message(Command("admin"), F.from_user.id in ADMINS_LIST)
async def cmd_admin(message: Message):
    await message.answer(f" all games: {all_games}")