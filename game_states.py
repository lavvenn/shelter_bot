from aiogram.fsm.state import StatesGroup, State

class Game(StatesGroup):
    game_configuration = State()
    game = State()