from aiogram import Router
import aiogram
from aiogram.filters import CommandStart
from aiogram.types import Message
from lexicon.lexcion_ru import LEXICON
from keyboards.main import main_menu
from keyboards.tests import tests
from aiogram.types import CallbackQuery
from aiogram import F

main_router = Router()

# Этот хэндлер срабатывает на команду /start
@main_router.message(CommandStart())
async def process_start_command(message: Message):
    keyboards = main_menu()
    await message.answer(text=LEXICON['/start'], reply_markup=keyboards)

@main_router.callback_query(F.data.in_({"tests", "train_biling", "results"}))
async def process_menu(callback: CallbackQuery):
    if callback.data == "tests":
        keyboards = tests()
        await callback.message.answer(LEXICON[callback.data + '_answer'], reply_markup=keyboards)
        await callback.answer()


