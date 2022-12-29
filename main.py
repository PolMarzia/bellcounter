import telebot
import CONFIG
token = CONFIG.TOKEN

bot = telebot.TeleBot(token)
mas = 0

@bot.message_handler(commands=["open"])
def start(message):
    global mas
    mas = 0
    bot.send_message(message.chat.id,
                     text="Смена открыта! Счетчик колоколов обнулен.")

@bot.message_handler(commands=["colocol"])
def colocol(message):
    global mas
    mas+=1
    bot.send_message(message.chat.id,
                     text="Колокол! Колоколов уже было: " + str(mas))
@bot.message_handler(commands=["close"])
def close(message):
    global mas
    bot.send_message(message.chat.id,
                     text="Смена закончена. Колоколов сегодня было: " + str(mas))
    mas = 0

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)