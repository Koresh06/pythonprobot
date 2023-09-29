from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, CommandStart


from app.keyboards import kb, kb_in

router = Router()

class Register(StatesGroup):
    name = State()
    carrency = State()
    balance = State()
    confirmation = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name} !', reply_markup=kb.but_menu)


@router.message(Command('register'))
async def cmd_regiter_name(message: Message, state: FSMContext):
    await message.answer(text='Введите название счёта')
    await state.set_state(Register.name)
    
@router.message(Register.name)
async def cmd_currency(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Выбирите валюту', reply_markup=kb_in.in_kb)
    await state.set_state(Register.carrency)
    
    
@router.message(Register.carrency)
async def cmd_carrency(message: Message, state: FSMContext):
    await state.update_data(carrency=message.text)
    await message.answer(text='Первоначальный баланс') 
    await state.set_state(Register.balance)
       
@router.message(Register.balance)
async def cmd_balance(message: Message, state: FSMContext):
    await state.update_data(balance=message.text)
    await message.answer(text='Подтвердите Ваш выбор')
    await state.set_state(Register.confirmation)
    
@router.message(Register.confirmation)
async def cmd_confirmation(message: Message, state: FSMContext):
     user_data = await state.get_data()
     await message.answer(
         text=f'Ваши указанные данные {user_data}'
     )
     await state.clear()