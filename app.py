import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


TOKEN = '6806758618:AAGfqwxt2eBWYyKkJktkwOTONWv-M-UtbWg'

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    from handlers import dp

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())