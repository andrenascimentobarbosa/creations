import random
import string


def generate_password(length=12):
    try:
        # Define the character set for the password
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        print(f'Password generated: \033[1m{password}\033[m')

    except Exception as e:
        print(f'Error: {e}')
