import random
import string

def random_string() -> tuple[str, str]:
    
    length = random.randint(50, 100)
    characters = string.ascii_uppercase + string.digits + string.punctuation
    target_character = random.choice(characters)
    random_str = ''.join(random.choices(characters, k=length))
    return target_character, random_str

def get_amount_in_random_string(random_string: str, target_character: str) -> int:
    return random_string.count(target_character)