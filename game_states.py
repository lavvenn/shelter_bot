from aiogram.fsm.state import StatesGroup, State

class Game(StatesGroup):
    game_configuration = State()
    join_game = State()
    waiting_for_players = State()

    game = State()