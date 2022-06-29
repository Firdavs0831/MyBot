from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

btn = InlineKeyboardMarkup(
    inline_keyboard=(
        [InlineKeyboardButton(text="bot haqida",callback_data="malumot")],
        [InlineKeyboardButton(text="botni kim yasagan",callback_data="Firdavs")],
        [InlineKeyboardButton(text="gurpaga ulashish",switch_inline_query="Assalomu alaykum")],
        [InlineKeyboardButton(text="gurpaga qoshish",url="https://t.me/snifdoshlar2001_bot?startgroup=2001-yillar")],
    )
)
