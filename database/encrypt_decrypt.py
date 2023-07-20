import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# Функция для шифрования данных
def encrypt_data(data):
    cipher_suite = Fernet(os.getenv("ENCRYPTION_KEY"))
    encrypted_data = [cipher_suite.encrypt(item.encode()) for item in data]
    return encrypted_data

# Функция для дешифрования данных
def decrypt_data(encrypted_data):
    cipher_suite = Fernet(os.getenv("ENCRYPTION_KEY"))
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data