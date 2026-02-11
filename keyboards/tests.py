from keyboards.inline_builder import create_inline_kb
from aiogram.types import InlineKeyboardMarkup

def tests() -> InlineKeyboardMarkup:
    return create_inline_kb(
        1,
        'test_2',
        'test_4'
    )

def start_test() -> InlineKeyboardMarkup:
    return create_inline_kb(
        1,
        'start_test'
    )