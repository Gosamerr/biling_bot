from aiogram import Router
import aiogram
from aiogram.filters import Command, CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message
from lexicon.lexcion_ru import LEXICON
from keyboards.main import main_menu
from keyboards.tests import tests, start_test
from aiogram.types import CallbackQuery
from aiogram import F
from services.test4 import random_string, get_amount_in_random_string
from states.test4 import Test4
from aiogram.fsm.context import FSMContext
# Инициализируем роутер уровня модуля
router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboards = main_menu()
    await message.answer(text=LEXICON['/start'], reply_markup=keyboards)

@router.callback_query(F.data.in_({"tests", "train_biling", "results"}))
async def process_menu(callback: CallbackQuery):
    keyboards = tests()
    await callback.message.answer(LEXICON[callback.data + '_answer'], reply_markup=keyboards)
    await callback.answer()


@router.callback_query(F.data == "test_4")
async def process_start_test(callback: CallbackQuery):
    keyboards = start_test()
    await callback.message.answer(text=LEXICON[callback.data + '_answer'], reply_markup=keyboards)
    await callback.answer()

@router.callback_query(F.data == "start_test")
async def process_start_test(callback: CallbackQuery, state: FSMContext):
    target_character, random_str = random_string()

    await state.update_data(
        random_str=random_str,
        target_character=target_character
    )

    await state.set_state(Test4.waiting_for_answer)

    await callback.message.answer(f"{random_str}\n\nСколько раз встречается символ '{target_character}'?")
    await callback.answer()

@router.message(Test4.waiting_for_answer)
async def process_test_answer(message: Message, state: FSMContext):
    data = await state.get_data()

    random_str = data['random_str']
    target_character = data['target_character']

    amount = get_amount_in_random_string(random_str, target_character)

    if message.text.isdigit() and int(message.text) == amount:
        await message.answer(
            f"Правильно! 🎉\n"
            f"В строке {amount} вхождений символа '{target_character}'.\n\n"
            f"Чтобы вернуться в меню, нажмите /start"
        )
    else:
        await message.answer(
            f"Неправильно ❌\n"
            f"Правильный ответ: {amount}\n\n"
            f"Чтобы вернуться в меню, нажмите /start"
        )

    await state.clear()
