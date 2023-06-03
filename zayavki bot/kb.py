import telebot
from telebot import types
try:
    send_kb = types.InlineKeyboardMarkup(row_width=3)
    send_button = types.InlineKeyboardButton("🟢Отправить🟢", callback_data="send_to_admin")
    pass_button = types.InlineKeyboardButton("", callback_data='aue')
    send_kb.add(send_button, pass_button)

    choice = types.InlineKeyboardMarkup(row_width=3)
    button_accept = types.InlineKeyboardButton("🟢Принять🟢", callback_data='call_accept')
    button_decline = types.InlineKeyboardButton("🔴Отклонить🔴", callback_data='call_decline')
    choice.add(button_accept, button_decline)
except Exception as er:
    print(er)
