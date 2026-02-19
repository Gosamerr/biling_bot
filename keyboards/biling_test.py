from keyboards.inline_builder import create_inline_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexcion_ru import LEXICON
import random

def biling_menu() -> InlineKeyboardMarkup:
    return create_inline_kb(
        2,
        'eng-rus', 'rus-ka', 'rus-tt', 'rus-az', 'main_menu'
    )

def answer_buttons(correct_answer: str, wrong_answers: list[str]) -> InlineKeyboardMarkup:
    """Создаёт кнопки с вариантами ответов (перемешанные)"""
    all_answers = [correct_answer] + wrong_answers
    random.shuffle(all_answers)
    
    kb_builder = InlineKeyboardBuilder()
    
    for answer in all_answers:
        kb_builder.add(InlineKeyboardButton(
            text=answer,
            callback_data= f"{answer}"
        ))
    
    kb_builder.adjust(1) 
    return kb_builder.as_markup()

def biling_to_main() -> InlineKeyboardMarkup:
    return create_inline_kb(
        1,
        'train_biling', 'main_menu'
    )