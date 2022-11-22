import logging, settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename = 'bot.log', level = logging.INFO, format = FORMAT)

def greet_user(update, context):
    print('Call /start')
    update.message.reply_text('Hello user! You called command /start')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, use_context = True)

    logging.info('Bot started!')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()