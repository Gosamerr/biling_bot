import random
import requests
from pathlib import Path

_WORDS_FILE = Path(__file__).resolve().parent.parent / "russian.txt"
try:
    with _WORDS_FILE.open("r", encoding="utf-8") as ru:
        RUSSIAN_WORDS = {w.strip().lower() for w in ru if w.strip()}
except FileNotFoundError:
    RUSSIAN_WORDS = set()

def random_character() -> tuple[str, str]:
    
    characters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
    target_character = random.choice(characters)
    return target_character

def get_correct_words(string_of_words: tuple[str, ...], character: str) -> int:

    ch = character.lower()

    user_words = {w.lower() for w in string_of_words if w and w[0].lower() == ch}

    return len(user_words & RUSSIAN_WORDS)