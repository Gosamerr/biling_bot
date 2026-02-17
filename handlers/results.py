from aiogram import Router
from aiogram.types import Message
from lexicon.lexcion_ru import LEXICON
from keyboards.results import next_fact
from aiogram.types import CallbackQuery
from aiogram import F
from services.facts import Facts

results_router = Router()

@results_router.callback_query(F.data.in_({"facts", "next_fact"}))
async def process_facts(callback: CallbackQuery):

    keyboards = next_fact()

    fact = Facts.get_random_fact()

    await callback.message.answer(text=fact, reply_markup=keyboards)
    await callback.answer()
