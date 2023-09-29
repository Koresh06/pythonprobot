from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buttons = [
    [InlineKeyboardButton(text='BLR', callback_data='blr'),
     InlineKeyboardButton(text='USD', callback_data='usd')],
    [InlineKeyboardButton(text='EUR', callback_data='eur'),
     InlineKeyboardButton(text='RUB', callback_data='rub')]
]

in_kb = InlineKeyboardMarkup(inline_keyboard=buttons)