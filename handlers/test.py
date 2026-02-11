from aiogram import Router
from aiogram.types import Message
from lexicon.lexcion_ru import LEXICON
from keyboards.tests import start_test
from aiogram.types import CallbackQuery
from aiogram import F
from services.test2 import get_correct_words, random_character
from services.test4 import random_string, get_amount_in_random_string
from states.tests import Test4, Test2, Tests
from aiogram.fsm.context import FSMContext

test_router = Router()

@test_router.callback_query(F.data.startswith("test_") )
async def process_start_test(callback: CallbackQuery, state: FSMContext):

    keyboards = start_test()

    await state.set_state(Tests.test)
    await state.update_data(test=callback.data)

    await callback.message.answer(text=LEXICON[callback.data + '_answer'], reply_markup=keyboards)
    await callback.answer()

@test_router.callback_query(F.data == "start_test")
async def process_start_test(callback: CallbackQuery, state: FSMContext):

    data = await state.get_data()

    test = data['test']

    if test == "test_4":
        target_character, random_str = random_string()

        await state.update_data(
            random_str=random_str,
            target_character=target_character
        )

        await state.set_state(Test4.waiting_for_answer)

        await callback.message.answer(f"{random_str}\n\nСколько раз встречается символ '{target_character}'?")
    elif test == "test_2":
        target_character = random_character()

        await state.update_data(
            target_character=target_character
        )

        await state.set_state(Test2.waiting_for_answer)

        await callback.message.answer(f"Найдите все слова, начинающиеся на букву '{target_character}'")

    await callback.answer()

@test_router.message(Test4.waiting_for_answer)
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

@test_router.message(Test2.waiting_for_answer)
async def process_test_answer(message: Message, state: FSMContext):
    
    data = await state.get_data()

    target_character = data['target_character']
    string_of_words = message.text.split()

    amount = get_correct_words(string_of_words, target_character)

    if amount >= 10:
        await message.answer(f"Поздравляем! Вы набрали {amount} правильных ответов! 🎉")
    else:
        await message.answer(f"Вы набрали менее 10 правильных ответов = {amount}. Не отчаивайтесь, это всего лишь тест! Попробуйте снова или вернитесь в меню, нажав /start")

    await state.clear()