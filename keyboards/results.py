from keyboards.inline_builder import create_inline_kb
from aiogram.types import InlineKeyboardMarkup

from lexicon.lexcion_ru import LEXICON

def results_menu() -> InlineKeyboardMarkup:
    return create_inline_kb(
        2,
        'facts', 'staticts', 'main_menu'
    )

def next_fact() -> InlineKeyboardMarkup:
    return create_inline_kb(
        1,
        'next_fact','main_menu',
    )
