from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import CallbackQuery
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.menu import button
from keyboards.inline.mani import btn
@dp.message_handler(commands='2001B')
async def ikkimingbirlar(msg:types.Message):
    await msg.answer("do'stlarim",reply_markup=button)
@dp.message_handler(commands='malumot')
async def ikkimingbirlar(msg:types.Message):
    await msg.answer("bot haqida",reply_markup=btn)
@dp.message_handler(commands='qaytish')
async def bot(msg:types.Message):
    await msg.answer("qaytish",reply_markup=ReplyKeyboardRemove())
@dp.callback_query_handler(text='malumot')
async def info(call:CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("bot hozirda o'rganish uchun ishlatilyabti")
@dp.callback_query_handler(text='Firdavs')
async def info(call:CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("bu botni Firdavs yasagan")
