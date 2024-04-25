from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from config import ADMINS_LIST

from handlers.start import all_games

from keyboards import admin_kb as kb


router = Router()


#<--message handlers-->
@router.message(Command("admin"), F.from_user.id.in_(ADMINS_LIST))
async def cmd_admin(message: Message):
    await message.answer(f"{message.from_user.full_name} wlelcome, to admin panel!",
                          reply_markup=kb.admin_panel_kb)

#<--callback handlers-->
@router.callback_query(F.data == "get_active_games")
async def get_active_games(query: CallbackQuery):
    await query.message.edit_text(f"вот активные игры \n{all_games}", reply_markup=kb.back_kb)


@router.callback_query(F.data == "back_to_admin_panel")
async def back_to_admin_panel(query: CallbackQuery):
    await query.message.edit_text(f"{query.message.from_user.full_name} wlelcome, to admin panel!", reply_markup=kb.admin_panel_kb)