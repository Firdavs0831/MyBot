from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import CommandStart

# http://t.me/snifdoshlar2001_bot?start=876709435
@dp.message_handler(CommandStart(deep_link= '876709435'))
async def start(msg:types.Message):
    await msg.answer("siz bu havolani Firdavdan olgansiz")
@dp.message_handler(commands='Rasmlar')
async def ikkimingbirlar(msg:types.Message):
    await msg.answer('hozircha rasimlar mavjud emas')
@dp.message_handler(commands='admin')
async def ikkimingbirlar(msg:types.Message):
    await msg.answer(f"Adminga yozing https://t.me/Fi1TDTUEnerg")
