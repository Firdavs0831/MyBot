from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(commands='yordam')
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/yordam - Yordam",
            "/Admin - Adminga murojat",
            "/2001B - sinfdoshlar",
            "/Rasmlar - rasimlar toplami",
            "/admin_uchun - guruh admini uchun ruhsatnomalar",
            "/admin - Adminga murojat",
            "/malumot - bot haqida")

    await message.answer("\n".join(text))
