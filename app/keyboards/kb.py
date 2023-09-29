from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from lexicon.lexicon import LEXICON


but_menu = [
    [KeyboardButton(text='/start'),
     KeyboardButton(text='/help'),
     KeyboardButton(text='/description')]
]

menu_button = ReplyKeyboardMarkup(keyboard=but_menu,
                                  resize_keyboard=True,
                                  one_time_keyboard=True,
                                  input_field_placeholder='Выберете одну из команд меню')

buttons = [
    [KeyboardButton(text='BLR'),
     KeyboardButton(text='USD')],
    [KeyboardButton(text='EUR'),
     KeyboardButton(text='RUB')]
]
but_reply = ReplyKeyboardMarkup(keyboard=buttons,
                                resize_keyboard=True,
                                input_field_placeholder='Выбирите валюту',
                                one_time_keyboard=True)