from aiogram import Router

from handlers.game import create, master, main, join

from . import start, admin

router = Router()

router.include_routers(master.router,
                       create.router,
                       join.router, 
                       main.router,
                       start.router,
                       admin.router
                        )