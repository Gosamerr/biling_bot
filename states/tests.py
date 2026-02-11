from aiogram.fsm.state import StatesGroup, State

class Test4(StatesGroup):
    waiting_for_answer = State()
    
class Test2(StatesGroup):
    waiting_for_answer = State()    

class Tests(StatesGroup):
    test = State()
