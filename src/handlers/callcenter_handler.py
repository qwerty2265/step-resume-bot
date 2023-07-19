from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import CallCenterState

async def callcenter_handler(msg: types.Message, state: FSMContext) -> None:
    keyboard_button1 = types.KeyboardButton(text='Вернуться в начало')
    keyboard_button2 = types.KeyboardButton(text='Вернуться к выбору филиала')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(keyboard_button1, keyboard_button2)

    # честно, я не понимаю в чем проблема, 
    # но если выставить табуляции, чтобы сообщение было на нужном уровне вложенности
    # текст съезжает вправо
    # так что пока будет так
    callcenter_info: str = 'Вы указали неверный город.'

    match msg.text.lower():
        case 'алматы':
            callcenter_info = '''
Алматы.
Канал карьерного центра:
https://t.me/+M-FBa3ByjddmYTIy

Телеграм:
@careerstep

Телефон/WhatsApp:
+7 771 726 50 38
            '''
        case 'астана':
            callcenter_info = '''
Астана.
Канал карьерного центра: 
https://t.me/+M-FBa3ByjddmYTIy

Телеграм:
@careerstep_astana

Телефон/WhatsApp:
+7 777 313 1999
            '''
        case 'караганда':
            callcenter_info = '''
Караганда.
Канал карьерного центра:
https://t.me/+M-FBa3ByjddmYTIy

Телеграм:
@Careerstep_krg

Телефон/WhatsApp:
+7 708 651 47 62
            '''
    await CallCenterState.CallCenterCity.set()
    return await msg.answer(callcenter_info, reply_markup=keyboard)