import sqlite3
import telebot as tb
from cfg import *
from dbinit import *
from kb import *
from telebot import types

def accept(message):
    botz.send_message(message.chat.id,  f"{message.text}\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nТак выглядит ваша заявка\nчтобы ввести её заново пропишите /start", reply_markup=send_kb)

@botz.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    if call.message:
        if call.data == "send_to_admin":
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            try:
                #отправление
                temp = [userinfo[0], userinfo[1]]
                cur.execute("INSERT INTO users (userid, name) VALUES (?,?)", temp)
                botz.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Заявка отправлена!")
                ztext = call.message.text.split("➖➖➖➖➖➖➖➖➖➖➖➖➖")[0]
                botz.send_message(6089704303, f"💥новая заявка от @{userinfo[1]}!\n {ztext}", reply_markup=choice)
                conn.commit()
            except Exception as er:
                print(er)
        if call.data == "call_accept":
            try:
                #Принятие
                namee = call.message.text.split(" @")
                namee = namee[1].split("!\n")[0]
                botz.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Заявка принята!")
                temp = [1, namee]
                cur.execute("UPDATE users SET status = ? WHERE name = ?", temp)
                conn.commit()
                cur.execute(f"SELECT * FROM users WHERE name = '{namee}'")
                send_id = cur.fetchall()[0][0]
                botz.send_sticker(send_id, "CAACAgIAAxkBAAEJJ15kdfGT2-Eq05o2fazt_HvpngU1BwACnhkAAnHxeUnvoHyjGHc1YC8E")
                botz.send_message(send_id, "❗Вашу заявку одобрили!\n❗Наш основной бот: ")

            except Exception as er:
                print(er)
        if call.data == "call_decline":
            botz.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text="💔Заявка отклонена!💔")

@botz.message_handler(commands=['start'])
def start_message(message):
    db_init()
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    global userinfo
    userinfo = [message.chat.id, message.from_user.username]

    try:
        db_init()
        cur.execute(f"SELECT userid FROM users WHERE userid = '{message.chat.id}'")
        if cur.fetchone() == None:
            botz.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEJJKZkdKP-WqeTq3W_RTzaydYxi8X-MwACRxwAAqogQUkQY1qYAvXpmy8E')
            botz.send_message(message.chat.id, "💡Добро пожаловать!\n👀Заполните заявку\n📥Опишите свой опыт\n⏳Сколько времени готовы уделать работе?\n❓Откуда узнали о нас?")
            botz.register_next_step_handler(message, accept)
        else:
            botz.send_message(message.chat.id, "ты уже отправлял заявку!")
    except Exception as er:
        print(er)

while True:
    try:
        botz.polling()
    except Exception as er:
        print(er)