from keyboards.inline_builder import create_inline_kb
from aiogram.types import InlineKeyboardMarkup

def main_menu() -> InlineKeyboardMarkup:
    return create_inline_kb(
        1,
        'tests', 'train_biling', 'results'
    )

def return_to_main_menu() -> InlineKeyboardMarkup:
    return create_inline_kb(
        1,
        'main_menu'
    )


