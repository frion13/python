# import logging
# import random
#
# from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
#
# reply_keyboard = [['/info', '/play', '/close']]
# stop_keyboard = [['/stop']]
#
# markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
# stop_markup = ReplyKeyboardMarkup(stop_keyboard, one_time_keyboard=False)
#
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
# )
#
# logger = logging.getLogger(__name__)
#
#
# TOKEN = '5848862768:AAEF2p4rJVvewH0I5TTi8Mv815GXg0UJ6c8'
#
# sweety = 150
# take_sweet = 0
# player_sweet = 0
# bot_sweet = 0
#
#
# def first_player(update, context):
#     random_num = random.randint(1, 2)
#     if random_num == 1:
#         player_turn(update, context)
#     else:
#         bot_turn(update, context)
#
# def player_turn(update, context):
#     global sweety
#     global take_sweet
#     global player_sweet
#     update.message.reply_text(f"Ваш ход. Сейчас на столе: {sweety} конфет")
#     update.message.reply_text("Сколько конфет вы возьмете? Можно взять от 1 до 28 конфет")
#     print(update)
#     print(context)
#     take_sweet = int(update.message.text)
#     while take_sweet >28 or take_sweet<0 or take_sweet>sweety:
#         update.message.reply_text("Введите цифру от 1 до 28")
#     sweety -=take_sweet
#     player_sweet +=take_sweet
#     if sweety>0:
#         bot_turn(update, context)
#     else:
#         update.message.reply_text(" Вы победили! УРА!")
#
#
#
#
#
# def bot_turn(update, context):
#     global sweety
#     global take_sweet
#     global bot_sweet
#     take_sweet = sweety % 29 if sweety % 29 !=0 else random.randint(1,28)
#     sweety -= take_sweet
#     bot_sweet += take_sweet
#     update.message.reply_text(f"Бот взял: {take_sweet} конфет. Нв столе осталось {sweety} конфет")
#     if sweety > 0:
#         player_turn(update, context)
#     else:
#         update.message.reply_text(" Бот победил!")
#
#
#
#
#
#
#
#
#
#
#
# def start(update, context):
#     update.message.reply_text(
#         "Привет! Это бот с игрой в конфеты! Нажмите info чтоб прочитать правила или play чтоб начать играть", reply_markup=markup)
#
#
#
#
#
#
#
#
# def stop(update, context):
#     update.message.reply_text("Удачи!", reply_markup=markup)
#     return ConversationHandler.END
#
#
# def info(update, context):
#     global sweety
#     update.message.reply_text(
#         f"Правила игры с конфетами: На столе {sweety} конфет. Далее по очереди из общей кучи забираете от 1 до 28 конфет. Побеждает тот, кто сможет забрать все последние конфеты.")
#
#
# def close(update, context):
#     update.message.reply_text("Спасибо за игру!", reply_makup=markup)
#
#
# play_handler = ConversationHandler(
#     entry_points=[CommandHandler('play', first_player)],
#
#     # Condition into the chat
#     states={
#         1: [MessageHandler(Filters.text & ~Filters.command, player_turn)],
#         2: [MessageHandler(Filters.text & ~Filters.command, bot_turn)],
#
#     },
#     # Point of command '/stop'
#     fallbacks=[CommandHandler("stop", stop)]
# )
#
#
# def main():
#     updater = Updater(TOKEN)
#     dp = updater.dispatcher
#     dp.add_handler(play_handler)
#     dp.add_handler(CommandHandler("info", info))
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("close", close))
#
#
#
#
#
#     updater.start_polling()
#     updater.idle()
#
#
#
# if __name__ == '__main__':
#     main()