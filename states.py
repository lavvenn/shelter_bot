from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

class game(FSMContext):
    game_configuration = State()
    game = State()