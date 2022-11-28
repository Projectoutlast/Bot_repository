
import logging, settings, ephem, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename = 'bot.log', level = logging.INFO, format = FORMAT)

dt_now = datetime.datetime.now()
format_date = dt_now.strftime('%Y/%m/%d')

def greet_user(update, context):
    print('Call /start')
    update.message.reply_text('Hello user! You called command /start')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def some_planet_info(update, context):
    text = update.message.text.split()
    list_of_planet = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    if text[1] in list_of_planet:
        text = getattr(ephem, text[1])
        final_text = text(format_date)
        const = ephem.constellation(final_text)
        update.message.reply_text(const)
    else:
        update.message.reply_text('This isn\'t in my list')


def main():
    mybot = Updater(settings.API_KEY, use_context = True)

    logging.info('Bot started!')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', some_planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()