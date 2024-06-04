from aiogram import Router

from handlers.game import master, main

from . import start, admin

router = Router()

router.include_routers(master.router, 
                        main.router,
                        start.router,
                        admin.router
                        )