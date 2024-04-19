from aiogram import Router, F
from aiogram.filters.command import Command, CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message):
    await message.answer(f"Hello, {message.from_user.full_name}!")

@router.message(Command(commands=["help"]))
async def cmd_help(message):
    await message.answer(f"Hello, {message.from_user.full_name}!")

@router.message(F.text == "🎮начать игру")
async def start_game(message):
    await message.answer(f"Hello, {message.from_user.full_name}!")