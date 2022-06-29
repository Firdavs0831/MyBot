from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(commands='admin_uchun')
async def bot_help(message: types.Message):
    text = (
        "/ban - ban berish",
        "/unban - banni qaytarish",
        "/set_title - belgilagan holda gruh nomini o'zgartirish",
        "/set_photo - belgilagan holda gruh rasimini o'zgartirish",
        "/set_description - biyoga joylash",


    )

    await message.answer("\n".join(text))