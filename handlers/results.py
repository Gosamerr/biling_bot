from aiogram import Router
from aiogram.types import Message, CallbackQuery
from lexicon.lexcion_ru import LEXICON
from keyboards.results import next_fact
from keyboards.main import return_to_main_menu, return_to_main_menu
from aiogram import F
from services.facts import Facts
from services.session_logger import get_stats_for_user

results_router = Router()


@results_router.callback_query(F.data.in_({"facts", "next_fact"}))
async def process_facts(callback: CallbackQuery):
    keyboards = next_fact()

    fact = Facts.get_random_fact()

    await callback.message.answer(text=fact, reply_markup=keyboards)
    await callback.answer()


@results_router.callback_query(F.data == "staticts")
async def process_stats(callback: CallbackQuery):

    keyboards = return_to_main_menu()

    stats = get_stats_for_user(callback.from_user.id)

    text = (
        "📊 Ваша статистика:\n\n"
        f"• Всего сессий тестов пройдено: {stats['total_sessions']}\n"
        f"• Средний результат билингв-теста: {stats['biling_avg'] * 100:.1f}% правильных ответов\n"
        f"• Среднее количество правильных слов в тесте на вербальную беглость: {stats['test_2_avg_words']}\n"
        f"• Доля корректных ответов в тесте на цифровую утомляемость: {stats['test_4_correct']}\n"
    )

    await callback.message.answer(text=text, reply_markup=keyboards)
    await callback.answer()
