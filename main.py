from aiogram import Bot, Dispatcher
import logging
import asyncio

from handlers import callback,comands
from config import TOKEN

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    try: 
        dp.include_router(comands.router)
        dp.include_router(callback.router)
        print('Bot start')
        await dp.start_polling(bot)
        await bot.session.close()
    except Exception as ex:
        print(f"Ошибка {ex}")
    finally:
        await bot.session.close()
        
if __name__=="__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('bot.log'),
            logging.StreamHandler()  # Оставляем для отладки
        ]
    )
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")