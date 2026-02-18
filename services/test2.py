import random
from pathlib import Path

def random_character() -> tuple[str, str]:
    
    characters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
    target_character = random.choice(characters)
    return target_character

_WORDS_FILE = Path(__file__).resolve().parent.parent / "russian.txt"
_WORDS_BY_LETTER: dict[str, set[str]] = {}

def _load_words_for_letter(ch: str) -> set[str]:
    ch = ch.lower()
    if ch in _WORDS_BY_LETTER:
        return _WORDS_BY_LETTER[ch]

    words_for_letter: set[str] = set()
    try:
        with _WORDS_FILE.open("r", encoding="utf-8") as ru:
            for line in ru:
                w = line.strip()
                if not w:
                    continue
                if w[0].lower() == ch:
                    words_for_letter.add(w.lower())
    except FileNotFoundError:
        return set()

    _WORDS_BY_LETTER[ch] = words_for_letter
    return words_for_letter

def get_correct_words(string_of_words: tuple[str, ...], character: str) -> int:
    if not character:
        return 0

    ch = character[0].lower()
    dict_words = _load_words_for_letter(ch)
    if not dict_words:
        return 0

    user_words = {w.lower() for w in string_of_words if w and w[0].lower() == ch}
    return len(user_words & dict_words)
