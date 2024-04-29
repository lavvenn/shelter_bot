from aiogram.fsm.state import StatesGroup, State

class Game(StatesGroup):
    configuration = State()
    join = State()
    waiting = State()

    game = State()