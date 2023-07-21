import os
from dotenv import load_dotenv
from typing import Final, Dict, List
from cryptography.fernet  import Fernet

load_dotenv()
key = os.getenv("ENCRYPTION_KEY")

def encrypt_string(string) -> str:
    # Зашифровать строку
    if isinstance(string, str):
        encoded_string = string.encode('utf-8')

    elif isinstance(string, bytes):
        encoded_string = string
        
    f = Fernet(key)
    encrypted_string = f.encrypt(encoded_string)

    return encrypted_string

def encrypt_dict(dict: Dict[str, str]) -> Dict[str, str]:
    # Зашифровать словарь
    encrypted_dict = {}

    for key, value in dict.items():
        if key == "phone_number":
            encrypted_dict[key] = value
        else:
            encrypted_value = encrypt_string(value)
            encrypted_dict[key] = encrypted_value
    
    return encrypted_dict
    
def decrypt_string(encrypted_string) -> str:
    # Расшифровать строку
    try:
        f = Fernet(key)
        decrypted_string = f.decrypt(encrypted_string)
        decoded_string = decrypted_string.decode('utf-8')
        return decoded_string
    except:
       decrypted_string = f.decrypt(encrypted_string)
       return decrypted_string

def decrypt_dict(encrypted_dict: Dict[str, str]) -> Dict[str, str]:
    # Расшифровать словарь
    decrypted_dict = {}

    for key, encrypted_value in encrypted_dict.items():
        decrypted_value = decrypt_string(encrypted_value)
        decrypted_dict[key] = decrypted_value

    return decrypted_dict

def decrypt_list(encrypted_list: List[str]) -> List[str]:
    # Расшифровать список
    decrypted_list = []

    for encrypted_value in encrypted_list:
        decrypted_value = decrypt_string(encrypted_value)
        decrypted_list.append(decrypted_value)

    return decrypted_list
