from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name} !',
                         reply_markup=kb.main)
