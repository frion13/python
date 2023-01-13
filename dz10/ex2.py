
import logging
from random import randint
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)

reply_keyboard = [['/play', '/rules'],
                  ['/exit', ]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

TOKEN = '5848862768:AAEF2p4rJVvewH0I5TTi8Mv815GXg0UJ6c8'

def start(update, context):
    update.message.reply_text(
        "Приветствую! Предлагаю поиграть\n/play - начать игру\n/rules - правила игры\n/exit - выход",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def play(update, context):
    update.message.reply_text("Введите количество конфет")
    return 1


def get_candy(update, context):
    global candy
    try:
        candy = int(update.message.text)
        update.message.reply_text(
            f"В игре {candy} конфет\nВы ходите первым, сколько конфет вы возьмете")
        return 2
    except ValueError:
        update.message.reply_text(
            f"Вы ввели не число.\nВведите количество конфет")
        logging.warning("Ошибка: неверный тип данных")


def get_user_hod(update, context):
    global candy
    try:
        if 1 <= int(update.message.text) <= 28:
            new_candy = int(update.message.text)
            if new_candy > candy:
                update.message.reply_text(f"Введите {candy}")
                return 2
            candy -= new_candy
            if candy <= 28:
                update.message.reply_text(
                    "Вы проиграли.\nНажмите /play чтобы с играть ещё или /exit чтобы завершить")
                return ConversationHandler.END
            else:
                update.message.reply_text(
                    f"После вашего хода в корзине осталось {candy} конфет")
                if candy > 28:
                    candy_bot = candy % 29
                    if candy_bot == 0:
                        candy_bot = randint(1, 29)
                update.message.reply_text(f"Я беру {candy_bot} конфет")
                candy -= candy_bot
                update.message.reply_text(
                    f"После моего хода в корзине осталось {candy} конфет")
                if candy <= 28:
                    update.message.reply_text(
                        "Вы победили.\nНажмите /play чтобы с играть ещё или /exit чтобы завершить")
                    return ConversationHandler.END
                else:
                    update.message.reply_text(
                        "Введите количество конфет которое хотите взять")
                return 2
        else:
            update.message.reply_text(f"Введите число от 1 до 28")
            logging.warning("Ошибка: Введено не правильное число")
    except ValueError:
        update.message.reply_text(
            f"Вы ввели не число.\nВведите количество конфет")
        logging.warning("Ошибка: неверный тип данных")


def rules(update, context):
    update.message.reply_text(
        "Это игра с чат ботом. Вам предлагается ввести сколько конфет будет в игре.")
    update.message.reply_text(
        "После чего, вы по очереди берете конфеты с ботом от 1 до 28.")
    update.message.reply_text("Кто заберет последние конфеты тот и победил!")


def exit(update, context):
    update.message.reply_text("Счастливо!")


def stop(update, context):
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, get_candy)],

            2: [MessageHandler(Filters.text & ~Filters.command, get_user_hod)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(play_handler)

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()