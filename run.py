import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
import config

from app.handlers import router


load_dotenv(find_dotenv())

async def main():
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()
    
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
