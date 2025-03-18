import logging
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate
import app.keyboards as kb

# Настройка логирования
logger = logging.getLogger(__name__)

router = Router()

class Gen(StatesGroup):
    wait = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    logger.info("Пользователь начал взаимодействие")
    await message.answer("Добро пожаловать, Напишите ваш запрос")

@router.message(Gen.wait)
async def stop_flood(message: Message):
    logger.info("Пользователь отправил запрос во время генерации")
    await message.answer("Подождите, ваш запрос генерируется")

@router.message(Command('help'))
async def cmd_help(message: Message):
    logger.info("Пользователь запросил помощь")
    await message.answer('Вы нажали на кнопку помощи. Если у вас не работают кнопки, вводите их названия вручную')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    logger.info("Пользователь запросил каталог")
    await message.answer('Выберите писателя', reply_markup=kb.catalog)

@router.message(F.text == 'О нас')
async def about_us(message: Message):
    logger.info("Пользователь запросил информацию о нас")
    await message.answer('Это телеграм-бот для общения с известными писателями', reply_markup=kb.catalog)

@router.message(F.text == 'Помощь')
async def help_info(message: Message):
    logger.info("Пользователь запросил помощь")
    await message.answer('Вы нажали кнопку помощи. Если у вас не работают кнопки, вводите их названия вручную', reply_markup=kb.catalog)

@router.callback_query(F.data == 'ltolstoy')
async def lev_t_choose(callback: CallbackQuery):
    logger.info("Пользователь выбрал Льва Толстого")
    await callback.answer('Вы выбрали Льва Толстого', show_alert=True)
    await callback.message.answer('Вы выбрали Льва Толстого.')

@router.callback_query(F.data == 'atolstoy')
async def a_t_choose(callback: CallbackQuery):
    logger.info("Пользователь выбрал Алексея Толстого")
    await callback.answer('Вы выбрали Алексея Толстого', show_alert=True)
    await callback.message.answer('Вы выбрали Алексея Толстого.')

@router.callback_query(F.data == 'fmdostoevsckiy')
async def fm_dost_choose(callback: CallbackQuery):
    logger.info("Пользователь выбрал Ф.М. Достоевского")
    await callback.answer('Вы выбрали Ф.М. Достоевского', show_alert=True)
    await callback.message.answer('Вы выбрали Ф.М. Достоевского.')

@router.message()
async def generating(message: Message, state: FSMContext):
    logger.info("Начало генерации ответа")
    await state.set_state(Gen.wait)
    try:
        response = await ai_generate(message.text)
        await message.answer(response, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Ошибка при генерации ответа: {e}")
        await message.answer("Произошла ошибка при генерации ответа. Пожалуйста, попробуйте позже")
