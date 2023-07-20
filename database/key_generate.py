import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

# генерация ключа для шифрования данных, если таковой отсутствует

def key_generate() -> None:
    if os.getenv('ENCRYPTION_KEY') is None:
        with open('.env', 'a') as env_file:
            env_file.write(f"\nENCRYPTION_KEY={Fernet.generate_key().decode()}")