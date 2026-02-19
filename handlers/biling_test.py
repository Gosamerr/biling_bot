from aiogram import Router
from aiogram.types import Message
from keyboards.main import main_menu
from lexicon.lexcion_ru import LEXICON
from keyboards.tests import start_test
from aiogram.types import CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from states.tests import Biling_Test
from services.biling_test import BilingTest
from services.session_logger import log_biling_session
from keyboards.biling_test import answer_buttons, biling_to_main

biling_router = Router()

@biling_router.callback_query(F.data.in_({"eng-rus", "rus-ka", "rus-tt", "rus-az"}))
async def process_choice_lang(callback: CallbackQuery, state: FSMContext):
    """Начало теста - выбор языковой пары"""
    question_set, answer_set = BilingTest.get_questions(language=callback.data)

    await state.set_state(Biling_Test.biling_test)
    await state.update_data(
        questions=question_set,
        answers=answer_set,
        current_question=0,
        correct_answers=0,
        language_pair=callback.data
    )

    first_question = question_set[0]
    wrong_answers = BilingTest.get_random_answer(answer_set[0])
    
    keyboard = answer_buttons(answer_set[0], wrong_answers)
    
    # Сохраняем правильный ответ и варианты для проверки
    await state.update_data(
        correct_answer=answer_set[0],
        all_answers=[answer_set[0]] + wrong_answers
    )
    
    await callback.message.answer(
        text=f"🎯 Вопрос 1 из 3:\n\n{first_question}\n\nВыберите ответ:",
        reply_markup=keyboard
    )
    await callback.answer()

@biling_router.callback_query( Biling_Test.biling_test)
async def process_test_answer(callback: CallbackQuery, state: FSMContext):
    """Обработка выбранного ответа"""
    data = await state.get_data()
    
    question_set = data['questions']
    answers_set = data['answers']
    current_question = data['current_question']
    correct_answers = data['correct_answers']
    correct_answer = data['correct_answer']
    selected_answer = callback.data
    
    # Проверяем правильность
    if selected_answer == correct_answer:
        correct_answers += 1
        feedback = "✅ Правильно!"
    else:
        feedback = f"❌ Неправильно!\nПравильный ответ: {correct_answer}"
    
    current_question += 1
    
    if current_question < len(question_set):
        # Следующий вопрос
        next_question = question_set[current_question]
        next_answer = answers_set[current_question]
        wrong_answers = BilingTest.get_random_answer(next_answer)
        
        keyboard = answer_buttons(next_answer, wrong_answers)
        
        # Обновляем state с новыми данными
        await state.update_data(
            current_question=current_question,
            correct_answers=correct_answers,
            correct_answer=next_answer,
            all_answers=[next_answer] + wrong_answers
        )
        
        await callback.message.answer(text=feedback)
        await callback.message.answer(
            text=f"🎯 Вопрос {current_question + 1} из 3:\n\n{next_question}",
            reply_markup=keyboard
        )
    else:
        # Тест завершён
        keyboard = biling_to_main()
        score = f"{correct_answers} из {len(question_set)}"

        # Логируем результат в текстовый файл session.txt
        log_biling_session(
            tg_id=callback.from_user.id,
            language_pair=data["language_pair"],
            score=correct_answers,
            total_questions=len(question_set),
        )

        await callback.message.answer(text=feedback)
        await callback.message.answer(
            text=f"🏁 Тест завершён!\n"
            f"✅ Правильных ответов: {score}\n\n"
            f"Что бы потоврить тест, нажмите кнопку ниже ⬇️",
            reply_markup=keyboard, parse_mode="HTML"
        )
        await state.clear()
    
    await callback.answer() 
