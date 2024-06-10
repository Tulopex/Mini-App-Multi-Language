import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token="")
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    web_app_url = 'https://www.youtube.com'
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Запустить", web_app=WebAppInfo(url=web_app_url))]
    ])
    await message.answer('Добро пожаловать!\nЭто Mini App внутри Telegram', reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())