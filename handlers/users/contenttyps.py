from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text

@dp.message_handler(Text(contains='bot'))
async def bot(msg:types.Message):
    await msg.answer("Chaqirdingizmi /yordam")
@dp.message_handler(Text(contains='salom'))
async def bot(msg:types.Message):
    await msg.answer(f"Assalomu Alaykum  botga hush kelibsiz \n  {msg.from_user.full_name}")
@dp.message_handler(Text(contains='.'))
async def bot(msg:types.Message):
    await msg.answer('nima bu')
@dp.message_handler(content_types="voice")
async def bot2(msg:types.Message):
    await msg.answer(" Siz ovozli habar jonattingiz")
@dp.message_handler(content_types="audio")
async def bot2(msg:types.Message):
    await msg.answer(" Siz audio habar jonattingiz")
@dp.message_handler(content_types="sticker")
async def bot2(msg:types.Message):
    await msg.answer(" Siz sticker habar jonattingiz")
@dp.message_handler(content_types="EMOJI")
async def bot2(msg:types.Message):
    await msg.answer(" Siz ovozli habar jonattingiz")