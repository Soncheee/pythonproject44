import logging
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

# Настройка логирования
logger = logging.getLogger(__name__)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Недавние')],
                                     [KeyboardButton(text='Помощь'),
                                      KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лев Толстой', callback_data='ltolstoy')],
    [InlineKeyboardButton(text='Алексей Толстой', callback_data='atolstoy')],
    [InlineKeyboardButton(text='Ф.М.Достоевский', callback_data='fmdostoevsckiy')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Найти писателя',
                                                           request_contact=True)]],
                                 resize_keyboard=True)

logger.info("Клавиатуры успешно инициализированы")


