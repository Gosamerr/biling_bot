import random
import requests

def random_character() -> tuple[str, str]:
    
    characters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
    target_character = random.choice(characters)
    return target_character

def get_correct_words(string_of_words: tuple[str, ...], character: str) -> int:

    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

    text = response.content.decode('cp1251')

    with open('russian.txt', 'wb') as ru:
        ru.write(text.encode('utf-8'))

    with open('russian.txt', 'r', encoding='utf-8') as ru:
        words = ru.read().splitlines()

    correct_words = []
    for word in words:
        if word.lower().startswith(character.lower()) and word.lower() in [w.lower() for w in string_of_words]:
            correct_words.append(word)

    return len(correct_words)