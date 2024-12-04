from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью')


# @dp.message_handler(text=['Urban', 'ff'])
# async def urban_message(message):
#     print('Urban message')
#     await message.answer('Urban message')


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7890890424:AAEwL3AvXADeymJq1hsVzEH_kAkWYnGdBsc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer('Рады вас видеть')

@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print('Urban message')
    await message.answer('Urban message')


@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer(message.text.upper())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
"""
