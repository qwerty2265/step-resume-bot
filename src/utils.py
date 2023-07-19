def contains_phone_number(input_string: str) -> bool:
    # Проверка на наличие только цифр и знака "+" в начале строки
    allowed_characters = "0123456789"
    if input_string[0] not in allowed_characters and input_string[0] != "+":
        return False
    for char in input_string[1:]:
        if char not in allowed_characters:
            return False

    return True

def correct_length_phone_number(input_string: str) -> bool:
    # Проверка на пустую строку
    if not input_string:
        return False
    
    # Проверка на нужную длину номера (в данном случае минимальная длина казахстанского номера - 11)
    if len(input_string) < 11:
        return False
    
    return True

def count_spaces_inside_string(input_string: str) -> int:
    # Используем метод .strip() для удаления пробелов с обоих сторон строки
    # Затем сравниваем длину исходной строки с длиной строки без пробелов по краям
    # Разница между ними и будет количеством пробелов внутри строки
    return len(input_string) - len(input_string.strip(' '))
    
def contains_only_letters(input_string: str) -> bool:
    # Удаление пробелов в строке 
    input_string_no_spaces = ''.join(input_string.split())

    # Проверка на наличие только букв в строке
    return input_string_no_spaces.isalpha()