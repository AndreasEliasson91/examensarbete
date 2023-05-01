import json
import random
import string

def generate_dict_keys(amount: int) -> None:
    strings = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(amount)]

    with open(f'src/data/json/{amount}_dict_keys.json', 'w') as f:
        json.dump(strings, f)
